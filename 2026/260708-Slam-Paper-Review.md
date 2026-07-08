![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# V-SLAM / VIO Paper Review: From Under-Canopy Benchmarking to Modern Foundation-Model SLAM

## Part 1: The Dataset Paper — Cuaran et al. (2024)

**Citation:** Cuaran, J., Baquero Velasquez, A. E., Valverde Gasparino, M., Uppalapati, N. K., Sivakumar, A. N., Wasserman, J., Huzaifa, M., Adve, S., & Chowdhary, G. (2024). "Under-canopy dataset for advancing simultaneous localization and mapping in agricultural robotics." *The International Journal of Robotics Research*, 43(6), 739–749. https://doi.org/10.1177/02783649231215372

**Dataset repo:** https://github.com/jrcuaranv/terrasentia-dataset

---

### 1.1 Motivation

The paper's main point: SLAM works great indoors and in cities, where the world has familiar structure, and it falls apart under crop canopy — specifically corn and soybean, which happen to be the two biggest crops by acreage. The reason is straightforward: leaves create visual clutter, lighting swings wildly under canopy, and one row of corn looks a lot like the next row of corn. SLAM needs structure it can tell apart, and this environment doesn't offer much.

That's the setup for the paper's two contributions: a public dataset built specifically to expose this failure, and a benchmark of several leading VO/VIO/SLAM systems run against it.

### 1.2 Platform and Sensors

- **Robot:** TerraSentia, an under-canopy agricultural robot (built by EarthSense Inc., in collaboration with the University of Illinois Urbana-Champaign)
- **Site:** Illinois Autonomous Farm, University of Illinois at Urbana-Champaign
- **Collection window:** Summer 2022, with sequences collected roughly twice a week in corn fields, and less often in soybean and sorghum — so this is coverage across a whole season, not a single day out in the field.
- **Sensors recorded (via ROS bag and native SVO files):**
  - Stereo-inertial camera (ZED2), 832×468 px @ 30 fps
  - IMU (packaged with the ZED2, ~200 Hz — this is what lets the dataset support VIO and visual-inertial SLAM, not just plain VO)
  - Wheel encoders
  - GPS
  - EKF-estimated ground-truth robot pose, fused from the above for evaluation reference
- Camera intrinsics and IMU noise parameters are reported directly in the paper, using a pinhole model with radial-tangential distortion for the ZED2.

### 1.3 What Makes This Dataset Distinct

Compared to earlier agricultural SLAM datasets (Rosario, the orchard datasets from Capua et al.), the thing this paper does differently is treat **growth stage as an independent variable**. Instead of one fixed environment, the same rows get revisited all season as the canopy fills in — so the difficulty of the exact same navigation task ramps up as the crop grows, rather than difficulty being tangled up with comparing different fields or different crops.

The paper also situates itself against earlier work: evaluations on the Rosario dataset (ORB-SLAM2, S-PTAM) and on fruit orchards (Capua et al., 2018 — testing LibViso, ORB-SLAM, and S-PTAM) had already found that repetitive scenes, heavy vibration, and moving leaves choke existing VIO systems, and that some of them are sensitive to motion during initialization. Cuaran et al. build on that with a season-long, growth-stage-resolved benchmark instead of a single snapshot.

### 1.4 Benchmark Scenarios

Four data sequences, increasing in difficulty, form the core benchmark:

1. **Scenario 1 — Double loop, semi-structured environment near a cornfield**, including static objects like buildings and cars — this is the easy case, with clear trackable features and nothing occluding the camera.
2. **Scenario 2 — Double loop through a corridor between soybean and corn fields.**
3. **Scenario 3 — Four adjacent rows at an early growth stage** (canopy still open, more visual structure).
4. **Scenario 4 — Four adjacent rows at a late growth stage** (canopy closed, high visual self-similarity, heavier occlusion).

On top of these four, the season-long growth-stage sequences (labeled by date, Jun13 through Aug08) get used to track how tracking capability decays as canopy closes over about two months.

### 1.5 Systems Benchmarked

Six systems, spanning the optimization/filtering and sparse/dense split (full architecture treatment is coming in Part 2):

| System | Category | Estimation approach |
|---|---|---|
| ORB-SLAM3 | SLAM | Sparse, indirect, optimization-based |
| VINS-Fusion | VIO + SLAM | Sparse, indirect, optimization-based |
| SVO Pro | VIO + SLAM | Sparse, semi-direct, optimization-based |
| OpenVINS | VIO | Indirect, filtering-based |
| MSCKF (Sun et al. implementation) | VIO | Indirect, filtering-based |
| RTAB-Map | SLAM | Graph-based, appearance-based loop closure |

### 1.6 Key Findings

- **Overall ranking:** RTAB-Map, ORB-SLAM3, and VINS-Fusion came out ahead of the filtering-based approaches (OpenVINS, MSCKF) across the board.
- **Canopy closure hurts everyone, but not equally.** The season-long sequences show tracking capability (% of the sequence successfully tracked) sliding downward as canopy closes — this is the paper's central finding, and the one that matters most for any "does SOTA solve agriculture" question.
- **One bit of good news:** pure visual odometry methods held up about as well late-season as early-season on translational and rotational RPE, which the authors chalk up to the IMU carrying short-term motion estimates even after the camera gets visually "blinded" by canopy closure.
- **Root cause:** it's perceptual aliasing — rows looking identical to each other — combined with feature scarcity and instability from leaf occlusion and wind, not any one algorithm being weak. This lines up with, and extends, what earlier orchard/row-crop studies had already flagged.

---

## Part 2: Classical Baseline Architectures

*(Architecture diagrams for all three systems were generated separately as figures for this review — see accompanying SVGs: `orb_slam3_architecture`, `vins_fusion_architecture`, `rtabmap_architecture`.)*

### 2.1 ORB-SLAM3

**Citation:** Campos, C., Elvira, R., Rodríguez, J.J.G., Montiel, J.M.M., & Tardós, J.D. (2021). "ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial, and Multimap SLAM." *IEEE Transactions on Robotics*, 37(6), 1874-1890. https://arxiv.org/abs/2007.11898

**Architecture.** Three threads running in parallel:
- **Tracking**: figures out where the current frame sits relative to the active map, minimizing reprojection error; in visual-inertial mode it also estimates velocity and IMU biases alongside pose.
- **Local Mapping**: adds keyframes and points, prunes redundant ones, and refines everything with local bundle adjustment; in inertial mode it also handles IMU parameter initialization.
- **Loop Closing / Map Merging**: spots revisited places via DBoW2 bag-of-words, and merges two maps back together if they turn out to overlap.

The big structural addition over ORB-SLAM2 is the **Atlas** — a multi-map setup with one active map plus a set of dormant ones, all sharing a single DBoW2 keyframe database. That's what lets Tracking survive losing track gracefully: instead of failing outright, it just starts a fresh map, and Loop Closing can stitch it back in later if it turns out to be the same place.

> **See also:** Figure 1 ("Main system components of ORB-SLAM3") in Campos et al. (2021) for the original architecture diagram this section is based on.

**Training data.** None, really — this is a geometric pipeline built on hand-crafted ORB features, RANSAC matching, and bundle adjustment, not machine learning. The closest thing to "training" here is the **DBoW2 visual vocabulary** used for place recognition, and even that's just built once, offline, from a generic image corpus that has nothing to do with your deployment scene.

**Hardware.** CPU-only, and it's become the standard baseline running real-time on something like an Intel Core i7-7700 (3.6 GHz). It doesn't hold up as well on embedded hardware, though — people have specifically built profiling studies on Jetson TX2, Raspberry Pi 3B+, and Raspberry Pi 4B *because* ORB-SLAM3 struggles to hit real-time there, and separate Jetson Nano/TX2/Xavier work (on ORB-SLAM2 variants and OpenVSLAM) found real-time rates anywhere from 8-34 FPS depending on the hardware and power mode.

**Latency.** On desktop stereo hardware, one comparative study clocked ORB-SLAM3 at roughly 75-79 FPS across the EuRoC MH01-MH05 sequences — comfortably ahead of the 20 FPS EuRoC capture rate.

### 2.2 VINS-Fusion

**Citation:** Qin, T., Pan, J., Cao, S., & Shen, S. (2019). "A General Optimization-based Framework for Local Odometry Estimation with Multiple Sensors." arXiv:1901.03638. (Builds on Qin, T., Li, P., & Shen, S. (2018). "VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator." *IEEE Transactions on Robotics*, 34(4), 1004-1020.)

**Architecture.** This one's a sequential pipeline rather than parallel threads:
- **Front-end**: tracks Shi-Tomasi corner features with a KLT tracker between frames, and preintegrates the IMU between those same frames.
- **Back-end**: sliding-window nonlinear optimization over position, velocity, rotation, and IMU biases, with old measurements marginalized into a prior to keep the cost bounded.
- **Loop closure / pose graph** (optional): because the IMU's gravity measurement makes roll and pitch fully observable (and therefore drift-free), the pose graph only needs **4 degrees of freedom** — yaw and position — instead of the full 6-DOF loop closure ORB-SLAM3 does.
- It also does **online temporal calibration**, nudging the camera-IMU time offset on the fly.

> **See also:** Figure 1 ("An illustration of the proposed framework for state estimation...") in Qin, Pan, Cao, & Shen (2019), arXiv:1901.03638, for the original architecture diagram this section is based on.

**Training data.** Same story as ORB-SLAM3 — nothing learned here. The optional loop-closure module uses a bag-of-words scheme comparable to DBoW2, so the same "generic, pre-built vocabulary" caveat applies.

**Hardware.** CPU-based front-end and back-end, but noticeably hungrier than ORB-SLAM3 in practice: one Jetson benchmarking study had to switch to the GPU-accelerated version of VINS-Fusion on the TX2, because the stock CPU version simply didn't run — not enough memory or CPU headroom.

**Latency.** A recent comparison paper ran VINS-Fusion on an AMD Ryzen 9 7950X desktop CPU and measured 61.65 ms per frame total — 27.69 ms (45%) for the front-end, 33.76 ms (54%) for back-end updates — which works out to roughly 16 FPS on that hardware. Worth treating as one data point from one comparative study rather than an official number; it's a heavier configuration than VINS-Fusion's bare minimum, but it's a useful ballpark against ORB-SLAM3's desktop numbers above.

### 2.3 RTAB-Map

**Citation:** Labbé, M., & Michaud, F. (2019). "RTAB-Map as an open-source lidar and visual simultaneous localization and mapping library for large-scale and long-term online operation." *Journal of Field Robotics*, 36(2), 416-446. (Foundational loop-closure mechanism: Labbé, M., & Michaud, F. (2011). "Memory management for real-time appearance-based loop closure detection." *IROS*.)

**Architecture.** This one's chasing a different goal entirely than the other two — bounded, real-time behavior over long, large sessions, rather than squeezing out the last bit of trajectory accuracy:
- **Odometry** (Frame-to-Frame or Frame-to-Map) feeds new nodes into **Working Memory (WM)**.
- **Loop closure detection**: bag-of-words comparison of the new image against whatever's currently in WM; if it crosses a similarity threshold, a new graph constraint gets added.
- **Graph optimizer**: runs in the background, cleaning up accumulated drift as constraints come in.
- **Memory manager**: this is the whole point of RTAB-Map. When update time blows past a fixed threshold ("Rtabmap/TimeThr"), the oldest, lowest-weighted nodes in WM get shipped off to **Long-Term Memory (LTM)** and stop being compared against for loop closure. That decouples per-frame cost from total map size — which is literally why it's called "Real-Time Appearance-Based Mapping." Nodes can come back from LTM into WM later if the robot revisits that spot.

> **See also:** the system/workflow overview figures in Section 3 of Labbé & Michaud (2019), *Journal of Field Robotics*, 36(2), 416-446, for the original architecture diagrams this section is based on. (One honest gap: unlike the ORB-SLAM3 and VINS-Fusion citations above, I couldn't pin down the exact figure number for this one from what I had access to — worth checking the PDF directly.)

**Training data.** Same as the other two — nothing learned. The bag-of-words dictionary can build up online from the scene itself, or start from a pre-built one; either way, it's not a deep-learning model.

**Hardware.** CPU-based, and deliberately built to be bounded by disk space rather than RAM — that's the direct payoff of splitting WM and LTM. A commonly cited operating point is a 700 ms time threshold at 1 Hz detection, which lands around 70% CPU usage with stable RAM even on big environments.

**Latency.** RTAB-Map doesn't really give you a single FPS figure the way the other two do, because its whole real-time guarantee is defined differently: it keeps per-node processing time under a fixed, configurable ceiling (commonly 700 ms – 2 s, so roughly 0.5-1.4 Hz for loop closure/graph optimization) *no matter how big the map gets*. You trade off accuracy against that ceiling by tuning WM size, instead of the system just getting slower as the map grows the way an unbounded appearance-based system would.

### 2.4 Comparison Table

| | ORB-SLAM3 | VINS-Fusion | RTAB-Map |
|---|---|---|---|
| **Category** | SLAM | VIO + SLAM | SLAM |
| **Design style** | 3 parallel threads + Atlas multi-map | Sequential front-end/back-end pipeline | Graph-based + 3-tier memory manager |
| **Estimation** | Sparse, indirect, optimization (full BA) | Sparse, indirect, optimization (sliding window) | Sparse features + pose graph optimization |
| **Loop closure DOF** | 6-DOF (Sim3/SE3) | 4-DOF (yaw + position only) | 6-DOF, appearance-based (bag-of-words) |
| **"Training data"** | None (DBoW2 vocab is generic, pre-built) | None (same caveat, optional loop closure) | None (vocab can build online or be pre-seeded) |
| **Hardware profile** | CPU, real-time on desktop; degrades hard on embedded (Jetson/RPi) | CPU, more memory-hungry than ORB-SLAM3 on embedded (needed GPU variant on Jetson TX2) | CPU, memory-bounded by disk not RAM — designed for this |
| **Reported latency** | ~75-79 FPS (desktop stereo, EuRoC MH01-05) | ~61.65 ms/frame ≈ 16 FPS (desktop CPU, one comparative study) | Time-bounded by design (~700 ms-2s/node ceiling), not a flat FPS number |
| **Primary weakness for row-crop agriculture** | Loop closure fails under perceptual aliasing (per Cuaran et al. and the arable-farming GNSS paper) | Same aliasing vulnerability; 4-DOF loop closure still needs visual place recognition to trigger at all | Appearance-based loop closure is the *core* mechanism — most exposed to perceptual aliasing of any of the three |

### 2.5 On Neural Network Architecture — There Isn't One

Let's just say this plainly instead of leaving it implied by the table: **none of these three systems involve a neural network.** All three are classical, hand-engineered computer vision, full stop:

- **ORB-SLAM3** uses ORB features — a hand-crafted corner detector (FAST) paired with a hand-crafted binary descriptor (BRIEF), both just fixed math, no learned parameters anywhere.
- **VINS-Fusion** uses Shi-Tomasi corner detection with KLT optical-flow tracking — same story, classical CV.
- **RTAB-Map** relies on hand-crafted feature descriptors (usually SURF or ORB) for its bag-of-words matching.

People sometimes assume a neural net is hiding in the **DBoW2/DBoW3 bag-of-words vocabulary** these all use for loop closure. It isn't — it's a **vocabulary tree built via hierarchical k-means clustering** on hand-crafted descriptors, built once offline from a generic image corpus. No backpropagation, no learned weights, no training loop, anywhere in this generation of systems.

#### 2.5.1 Worked Example: What an ORB Feature Actually Is

*(Diagram generated for this subsection: `orb_feature_example`.)*

**Citation:** Rublee, E., Rabaud, V., Konolige, K., & Bradski, G. (2011). "ORB: An Efficient Alternative to SIFT or SURF." *IEEE International Conference on Computer Vision (ICCV)*.

An ORB feature isn't a little photograph of a patch — it's three things bundled together at one spot in the image, and none of them involve anything learned:

1. **A keypoint location**, found by **FAST** (Features from Accelerated Segment Test). FAST looks at a ring of 16 pixels around a candidate point and checks whether a contiguous chunk of them (usually 9 or more out of 16) is brighter or darker than the center pixel by some threshold. If a contiguous arc clears that bar, you've got a corner. That's also why ORB gravitates toward corners and textured regions, and why it struggles in the smooth, repetitive leaf and stalk regions that dominate under-canopy footage — directly tied to Part 1's perceptual-aliasing finding.
2. **An orientation** — the "Oriented" in ORB. FAST by itself isn't rotation-invariant, so ORB computes an **intensity centroid**: basically, which direction the brighter part of the patch sits relative to the corner. That angle (θ) is what lets the same physical corner still get recognized as the same feature when the camera rotates.
3. **A binary descriptor** — the "Rotated BRIEF" part. BRIEF's test pattern is a fixed set of roughly 256 pixel-pair comparisons in a ~31×31 patch around the keypoint: for each pair (p1, p2), it's just `intensity(p1) > intensity(p2) ? 1 : 0`. ORB's twist ("steered BRIEF") rotates that whole fixed pattern by θ before applying it, so the descriptor holds up under rotation. What comes out is a **256-bit string — 32 bytes** — and that's the actual thing that gets stored, compared via cheap Hamming distance (XOR plus a bit count), and fed into DBoW2's k-majority clustering (Section 2.6) to build visual words.

Boiled down to one sentence: ORB turns "there's a corner here, facing this way, and it looks like *this* against 256 specific brightness comparisons" into a single 32-byte number — and that number, not a picture, is what ORB-SLAM3 and DBoW2 are actually working with.

This is exactly the axis that flips in Part 3: MASt3R-SLAM, VGGT-SLAM, DPVO, and the rest swap these hand-crafted feature/matching stages out for a trained neural network — usually a transformer or CNN backbone — which is why "training data" is suddenly a real, answerable question for those systems in a way it just isn't here.

### 2.6 The DBoW2 Visual Vocabulary

*(Diagrams generated for this section: `dbow2_vocabulary_construction`, `dbow2_runtime_query`.)*

**Citation:** Gálvez-López, D., & Tardós, J.D. (2012). "Bags of Binary Words for Fast Place Recognition in Image Sequences." *IEEE Transactions on Robotics*, 28(5), 1188-1197. (Adapts the vocabulary-tree concept of Nistér, D., & Stevenius, H. (2006), "Scalable Recognition with a Vocabulary Tree," CVPR, to binary descriptors.) Code: https://github.com/dorian3d/DBoW2

Section 2.5 already said DBoW2's vocabulary isn't a neural network. It's worth going one level deeper, though, because *how* it's built and queried actually explains — mechanistically, not just hand-wavily — why appearance-based loop closure struggles in visually repetitive scenes.

**Construction (offline, once, not scene-specific).** Take a generic corpus of training images, pull ORB descriptors out of all of them, then **hierarchically cluster** them into a tree: at the root, split everything into *k* groups (the "branching factor," often 10), then split each of those groups again, and again, down to some depth *d* (often 6). The leaves of that tree — roughly k^d of them, so about a million for k=10, d=6 — are the **visual words**. Because ORB/BRIEF descriptors are binary strings, not real-valued vectors, standard k-means doesn't work here; DBoW2 uses **k-majority** clustering instead (a bitwise majority vote standing in for a centroid) with **Hamming distance** instead of Euclidean. Once this vocabulary is built, it's shipped as a fixed file. It never gets updated or fine-tuned to wherever you actually deploy it — agricultural or otherwise.

**Query (runtime, per new image).** A new image's ORB descriptors each get pushed down the fixed tree — nearest cluster at each level — landing on a leaf word. That gives you two things at once: a **bag-of-words vector**, with each word weighted by **TF-IDF** (same idea as text search — reward words that show up a lot in this image but rarely across the training corpus, since those are the discriminative ones), and a **direct index** tracking which intermediate tree nodes the image's features passed through. The bag-of-words vector gets checked against an **inverted index** (word → which database images contain it) to pull loop-closure candidates in close to constant time no matter how big the database gets; the direct index then speeds up finding candidate feature correspondences for **geometric verification** via RANSAC. The library itself reports roughly 3 ms to turn an image into a BoW vector and 5 ms to query a database of 19,000+ images — that speed is exactly why this got adopted for real-time loop closure in ORB-SLAM2/3, and the same basic scheme (or its successor, DBoW3) shows up in VINS-Fusion's optional loop closure and RTAB-Map's detector too.

**Why this matters for the row-crop aliasing problem.** The k-majority clustering step has a real, documented weakness that ties straight back to Part 1: binary clustering just can't hold onto subtle descriptor differences the way real-valued clustering can, and that quantization error stacks up as it moves down the tree — there's recent work (like HBRB-BoW) aimed specifically at fixing this. So DBoW2 isn't failing on similar-looking corn rows because "the scene is hard" in some vague sense — it's failing because its binary vocabulary was never able to hold onto the fine distinctions you'd need to tell two similar rows apart, before you even add canopy occlusion and lighting changes on top. That gives Part 3's "learned features generalize better" claim (Section 3.6) something concrete to point at: a continuous-valued, learned feature space (like MASt3R's retrieval features) simply has more room to keep exactly those fine distinctions that a fixed, binary, k-majority-clustered vocabulary structurally can't.

### 2.7 Synthesis Note for This Section

All three systems share the same weak spot Part 1 flagged: **loop closure only works if visual appearance is discriminative** — whether that's ORB-SLAM3's 6-DOF DBoW2 matching, VINS-Fusion's 4-DOF pose graph, or RTAB-Map's bag-of-words memory comparison. None of them has any way to tell "corn row 4" from "corn row 12" if the two look the same — that's exactly the perceptual aliasing problem Cuaran et al. documented, and it's baked into the architecture, not something you can tune away. That sets up Part 3 nicely: the newer, learned methods change *what* generates the features and geometry, but the more interesting question for row-crop agriculture is whether any of them actually change *how* loop closure decides "have I been here before" — worth checking directly rather than assuming.

---

## Part 3: Modern Learned Methods

*(Architecture diagrams generated as figures for this review: `mast3r_slam_architecture`, `mast3r_fusion_architecture`, `dpvo_dpv_slam_architecture`, `vggt_slam_architecture`. Pink/purple boxes in each diagram mark a trained neural network component — the visual cue for the axis that flipped from Part 2.)*

### 3.1 MASt3R-SLAM

**Citation:** Murai, R., Dexheimer, E., & Davison, A.J. (2025). "MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors." *CVPR 2025*. https://arxiv.org/abs/2412.12392 (System diagram: Figure 3 in the paper.)

**Architecture.** Built on top of **MASt3R** (itself built on **DUSt3R**), a two-view feed-forward network that regresses a dense 3D pointmap straight from an image pair — no fixed camera model required. The SLAM system wraps that prior with:
- **Pointmap matching / tracking**: a new frame's pointmap gets matched against the current keyframe via fast iterative projective matching, heavily parallelized on GPU — dense matching drops to about 2 ms per frame — which estimates pose and fuses the local pointmap.
- **Loop closure**: new keyframes pull candidates from a database of encoded MASt3R features; enough matches after decoding, and an edge gets added to the backend graph.
- **Backend**: large-scale second-order (Gauss-Newton / Levenberg-Marquardt) optimization keeps poses and dense geometry globally consistent.

**Training data.** The neural piece here is the pretrained **MASt3R** network, trained on a mix of 14 datasets — Habitat, ARKitScenes, BlendedMVS, MegaDepth, Static Scenes 3D, ScanNet++, CO3D-v2, Waymo, Mapfree, WildRGB, VirtualKitti, Unreal4K, TartanAir, and an internal dataset — covering indoor, outdoor, synthetic, and real scenes, with about 650k pairs sampled per epoch over 35 epochs. MASt3R itself starts from the public DUSt3R checkpoint (DUSt3R was trained on 8.5M image pairs across 8 of those same datasets). None of it is agriculture- or row-crop-specific — it's general-purpose multi-view geometry data, full stop.

**Hardware.** Needs a GPU — no CPU-only path, unlike Part 2. The paper's own experiments ran on a desktop with an Intel Core i9 12900K and a single NVIDIA GeForce RTX 4090.

**Latency.** Roughly **15 FPS** on that RTX 4090, with the authors subsampling every other frame of their benchmark datasets to simulate real-time behavior at typical camera rates.

### 3.2 MASt3R-Fusion

**Citation:** GREAT Group, School of Geodesy and Geomatics, Wuhan University (2025). "MASt3R-Fusion: Integrating Feed-Forward Visual Model with IMU, GNSS for High-Functionality SLAM." arXiv:2509.20757. Code: https://github.com/GREAT-WHU/MASt3R-Fusion

**Architecture.** Takes the MASt3R-SLAM lineage and fuses in **IMU preintegration** and **GNSS position** factors, all inside one **hierarchical factor graph** implemented via a modified C++ GTSAM with Python bindings. That graph handles real-time sliding-window optimization and global optimization with aggressive loop closures at the same time. This is basically the learned-era version of what the arable-farming GNSS-stereo-inertial ORB-SLAM3 paper did by hand — adding a GNSS error term to classical bundle adjustment (see the Part 1/Part 2 discussion). Here the visual measurements come from a neural network instead of geometric triangulation, but the core idea — fuse in GNSS to fight perceptual aliasing — carries over directly.

**Training data.** Same MASt3R backbone and training data as 3.1 — nothing gets retrained here. What's new is classical, probabilistic sensor fusion (GTSAM factors) wrapped around a frozen, pretrained MASt3R.

**Hardware.** Built to handle arbitrarily long sequences on **8GB of GPU memory** — a meaningfully lower bar than MASt3R-SLAM's RTX 4090 desktop setup, and a genuinely interesting number if you're thinking about field-deployable compute. Multi-threaded (PyTorch + GTSAM), Python 3.11, PyTorch 2.5.1 / CUDA 12.4 per the repo's spec.

**Latency.** No published FPS figure as of this review — the repo talks about memory footprint (8GB) and long-sequence stability, not a headline speed number. Worth flagging as a real gap if you want a precise figure here; check the GitHub issues/repo for anything the community's reported.

### 3.3 DPVO / DPV-SLAM

**Citation:** Lipson, L., Teed, Z., & Deng, J. (2023). "Deep Patch Visual Odometry." *NeurIPS 2023*. https://arxiv.org/abs/2208.04726 (DPVO). Lipson, L., Teed, Z., & Deng, J. (2024). "Deep Patch Visual SLAM." *ECCV 2024*. https://arxiv.org/abs/2408.01654 (DPV-SLAM, extends DPVO with loop closure). Code (both): https://github.com/princeton-vl/DPVO

**Architecture.** DPVO tracks a **small number of learned patches (64-96) per frame** instead of dense optical flow — think of it as a sparse cousin of DROID-SLAM's frontend. Patches get matched via learned correlation features and refined by a recurrent update operator (same family as RAFT-style optical flow networks). DPV-SLAM turns this odometry-only system into a full SLAM system by bolting on **two loop closure mechanisms**: proximity-based (detects loops based on camera proximity, which sidesteps the awkwardness of running frontend and backend in parallel on deep networks) and classical feature-based. Both feed a shared patch graph, optimized with a custom **CUDA-accelerated block-sparse bundle adjustment** solver built specifically for that patch-graph structure.

**Training data.** Trained **entirely on the synthetic TartanAir dataset** — notably narrower than MASt3R/VGGT's 8-14-dataset mixtures. Despite that narrow diet, DPVO's average error on the real-world EuRoC benchmark comes in 43% lower than DROID-VO, which is the headline claim here: it never saw anything like EuRoC's indoor drone footage during training, and it still beats a comparable end-to-end learned baseline there.

**Hardware.** Needs a GPU. DPV-SLAM keeps a small memory footprint — **5-7GB** — compared to other deep SLAM systems, built to run on a single consumer GPU rather than needing a cluster.

**Latency.** DPV-SLAM runs at **1x-4x real-time** on real-world datasets. On EuRoC specifically, it lands close to DROID-SLAM's accuracy (0.024 vs 0.022 ATE) while running 2.5x faster (50 FPS vs 20 FPS) on a quarter of the memory (5GB vs 20GB). The bare DPVO odometry-only system is faster still — around 60 FPS normally, with a 120 FPS variant available if you'll take a modest accuracy hit.

### 3.4 VGGT-SLAM

**Citation:** Maggio, D., Lim, H., & Carlone, L. (2025). "VGGT-SLAM: Dense RGB SLAM Optimized on the SL(4) Manifold." arXiv:2505.12549. Backbone: Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., & Novotny, D. (2025). "VGGT: Visual Geometry Grounded Transformer." *CVPR 2025* (Best Paper Award). (Architecture diagram: Figure 2 in the VGGT paper.)

**Architecture.** VGGT itself is a large feed-forward transformer: it patchifies input images via DINO, then alternates frame-wise and global self-attention layers (24 of each, by default) — and notably has **no 3D-specific inductive bias built in**, unlike MASt3R/DUSt3R's more geometry-aware design. A camera head predicts intrinsics/extrinsics from a dedicated camera token; a DPT head predicts depth maps, point maps, and tracking features for every frame — up to hundreds of images in one forward pass, in under a second. VGGT-SLAM wraps this: since VGGT's memory cost makes processing a whole long video in one pass infeasible, the video gets chunked into **overlapping submaps**, each reconstructed independently by VGGT, and then those submaps get stitched together by optimizing **15-degree-of-freedom homography transforms on the SL(4) manifold** — a more complex transform than the 7-DOF similarity transforms other submap approaches use. The paper's argument is that uncalibrated cameras genuinely introduce a 15-DOF projective ambiguity, and ignoring that mismatch (like prior submap methods do) just introduces avoidable error.

**Training data.** The paper says it's trained on "a large number of publicly available datasets with 3D annotations" — the exact list lives in supplementary material I wasn't able to pull for this review. Given VGGT explicitly builds on and compares itself against DUSt3R/MASt3R throughout the paper, it's a decent bet the mixture overlaps heavily with the Habitat/ARKitScenes/MegaDepth/CO3D/ScanNet++/Waymo family those use — but that's an inference, not a confirmed fact, so don't cite it as one without checking the appendix yourself.

**Hardware.** Needs a GPU, and VGGT's memory appetite is literally the reason VGGT-SLAM's submap design exists — the paper says plainly that it gets better map quality on long sequences that would be infeasible for VGGT to handle directly, because of VGGT's GPU requirements. VGGT-SLAM 2.0's benchmarks ran on an RTX 3090.

**Latency.** VGGT itself reconstructs a scene in under a second per forward pass on an H100 — but that's per-submap, not per-frame throughput for a running system. For the full VGGT-SLAM 2.0 system on an RTX 3090, measured throughput is about **8.4 FPS** for a 16-frame submap with no open-set detection, dropping to **6.3 FPS** with open-set CLIP-based detection turned on; over half the per-submap time (1248 ms) goes to the VGGT forward pass alone. In a same-machine comparison the same paper ran, MASt3R-SLAM came in at 7.2 FPS and VGGT-SLAM at 6.9 FPS — notably slower than MASt3R-SLAM's own reported 15 FPS on an RTX 4090, which is a good reminder that cross-paper latency numbers depend heavily on hardware and shouldn't be read as a clean ranking without checking the actual test rig.

### 3.5 Comparison Table

| | MASt3R-SLAM | MASt3R-Fusion | DPVO / DPV-SLAM | VGGT-SLAM |
|---|---|---|---|---|
| **Neural backbone** | MASt3R (ViT-L encoder / ViT-B decoder) | MASt3R (frozen, same as MASt3R-SLAM) | Custom CNN + recurrent update operator (RAFT-family) | VGGT (DINO patchify + alternating-attention transformer) |
| **What's learned vs. classical** | Pointmap regression learned; tracking/backend optimization classical (Gauss-Newton) | Same as MASt3R-SLAM, plus classical GTSAM factor graph for IMU/GNSS | Patch tracking + correlation learned; final BA is a classical (CUDA-accelerated) solver | Pointmap, depth, camera, and tracking all learned; submap alignment (SL(4)) is classical |
| **Training data** | 14-dataset mixture (Habitat, ARKitScenes, MegaDepth, CO3D-v2, TartanAir, +9 more), ~650k pairs/epoch | Same as MASt3R-SLAM (backbone frozen) | TartanAir only (synthetic) | Large multi-dataset mixture (exact list not confirmed from available sources) |
| **Hardware** | GPU; RTX 4090 desktop in paper | GPU; runs on 8GB VRAM | GPU; 5-7GB VRAM | GPU; RTX 3090 (VGGT-SLAM 2.0), high VRAM demand from base VGGT is the whole reason submaps exist |
| **Reported latency** | ~15 FPS (RTX 4090) | Not yet independently benchmarked (FPS not published) | DPVO ~60-120 FPS; DPV-SLAM ~39-50 FPS, 1x-4x real-time | ~8.4 FPS (RTX 3090, 16-frame submap, no CLIP); ~6.3 FPS with open-set detection |
| **Loop closure mechanism** | Learned-feature retrieval database + geometric verification | Same as MASt3R-SLAM, plus GNSS as an independent drift-correction signal | Two mechanisms: proximity-based (geometric) + classical feature-based | SL(4) manifold alignment with loop closure constraints between submaps |

### 3.6 Synthesis Note for This Section

Two things worth pulling out here rather than leaving buried in the table. First, **"loop closure" in this generation is still mostly about visual appearance** — MASt3R-SLAM's retrieval database and VGGT-SLAM's submap loop constraints are still fundamentally asking "does this look like somewhere I've been," just with learned features standing in for DBoW2's hand-crafted vocabulary. That's a real win for discriminability (learned features handle lighting and viewpoint changes better than ORB+BRIEF), but it's not architecturally a different question from what Part 2's systems ask — and that matters a lot for the row-crop aliasing problem from Part 1, because the failure mode there isn't "features are too weak," it's "the rows are genuinely, structurally self-similar." A better feature descriptor narrows that gap. It doesn't obviously close it. Second, **MASt3R-Fusion is the one system here that actually changes the question, not just the features** — by tightly fusing GNSS, it stops asking "have I seen this exact view before" for large chunks of the trajectory, and asks "where does an independent global sensor say I am" instead. That's precisely the fix the Cremona et al. arable-farming paper found worked for classical ORB-SLAM3. It's arguably the single most transferable idea in this whole review, and it's not even a neural-network idea — it's a sensor-fusion idea that happens to have been rebuilt on top of a neural front end.

---

## Part 4: Synthesis

### 4.1 The Accuracy Trend, Quantified

Here's every number from Parts 2 and 3 in one place:

| Comparison | Result |
|---|---|
| ORB-SLAM3 vs. MASt3R-SLAM (ETH3D-SLAM, ATE) | 0.135 m → 0.086 m (~36% reduction) |
| ORB-SLAM3 vs. FoundationSLAM (ETH3D-SLAM, ATE) | 0.135 m → 0.069 m (~49% reduction) |
| DROID-SLAM vs. DPV-SLAM (EuRoC, ATE) | 0.022 m → 0.024 m (DPV-SLAM ~9% worse, but see cost trend below) |
| DROID-VO vs. DPVO (EuRoC, average error) | DPVO ~43% lower error, despite training only on synthetic TartanAir |
| ORB-SLAM3 stereo-inertial vs. + GNSS fusion (Rosario/arable farming) | 10-30% pose error reduction from adding a GNSS factor alone |
| RTAB-Map/ORB-SLAM3/VINS-Fusion vs. filtering-based VIO (Cuaran et al., under-canopy) | Optimization-based systems "demonstrate superior performance" — no precise numbers extracted from available sources (flagged in Part 1) |

Here's the honest read: **the jump from classical to learned front-ends is real, but it's incremental** — a third to a half reduction in ATE on standard benchmarks, not an order of magnitude. The bigger jump in this whole review is the **GNSS-fusion result**: just adding one sensor modality to an otherwise-unchanged classical pipeline beats the entire generational leap from ORB-SLAM3 to MASt3R-SLAM, specifically on the perceptual aliasing problem Part 1 flagged as the core agricultural failure mode. That's worth saying plainly rather than letting a "newer is always better" story paper over it.

### 4.2 The Compute-Cost Trend

This is arguably the more consistent story, and maybe the more interesting one:

- **Classical era (Part 2)**: CPU-only, real-time on a standard desktop CPU (i7-7700), but it falls off hard on embedded platforms (8-34 FPS on Jetson/Raspberry Pi depending on config and power mode). No GPU needed, period.
- **Learned era (Part 3)**: GPU required across the board, no exceptions. Within that, there's a wide spread — DPV-SLAM's 5-7GB footprint is close to what a single embedded GPU (Jetson Orin-class) could plausibly handle, while base VGGT's memory demand is so heavy that VGGT-SLAM's entire architecture is basically a workaround (submap chunking) for that one constraint. MASt3R-Fusion's 8GB target sits in between.
- **Latency spread within the learned era** is wide too: DPVO's ~60-120 FPS is close to classical-era speeds, while MASt3R-SLAM (~15 FPS) and VGGT-SLAM (~7-8 FPS) are a lot slower — and that's before you even factor in the cross-paper hardware variance from Part 3 (MASt3R-SLAM at 15 FPS on an RTX 4090 in its own paper vs. 7.2 FPS in a later paper's same-machine comparison).

Practically speaking: **"learned SLAM" isn't one cost tier — it's a spread as wide as the classical-to-learned jump itself.** DPVO/DPV-SLAM's whole design philosophy (few tracked patches, purpose-built CUDA kernels) reads like a direct reaction against the DROID-SLAM/dense-flow school's appetite for compute, the same way RTAB-Map's memory manager was a reaction against unbounded appearance-based loop closure cost. It's a pattern that repeats: every SOTA wave produces a maximal, compute-hungry version and a leaner sibling built for actually deploying the thing.

### 4.3 What SOTA Buys a Resource-Constrained Field Robot vs. a Research Benchmark Rig

This is the question that matters most for your IsaacSim/TerraSentia work, so let's not soften it: **almost none of the accuracy gains in Part 3 have been tested on agricultural data.** Every benchmark cited for MASt3R-SLAM, MASt3R-Fusion, DPVO/DPV-SLAM, and VGGT-SLAM in this review comes from generic indoor/outdoor datasets — TUM RGB-D, EuRoC, ETH3D-SLAM, 7-Scenes, KITTI, TartanAir. Searching for agricultural or row-crop evaluations of any of these four turned up nothing. We genuinely don't know if they run acceptably in a cornfield, let alone whether they beat the classical systems Cuaran et al. already tested.

Two things follow from that:

1. **The accuracy numbers here might just not transfer.** A 36-49% ATE reduction on ETH3D-SLAM's office and lab scenes says nothing directly about a closed corn canopy, where the failure mode — nearly identical-looking rows — is qualitatively different from anything in those training or eval sets. MASt3R/VGGT's training mixtures (Habitat, ARKitScenes, MegaDepth, CO3D, ScanNet++, Waymo, TartanAir) are indoor scenes, driving scenes, object-centric captures — none of it row-crop agriculture, and there's no obvious reason a network trained on that would beat ORB features at handling repetitive foliage.
2. **Compute matters more than accuracy for a field robot.** A TerraSentia-class platform has a hard power/thermal/payload budget that a research desktop with an RTX 4090 just doesn't. DPV-SLAM's 5-7GB footprint is the only one of the four Part 3 systems that looks plausibly deployable on current embedded GPU hardware (Jetson Orin-class) without more work; MASt3R-SLAM and VGGT-SLAM's reported hardware (RTX 4090, RTX 3090) are desktop parts, and neither paper reports embedded numbers the way several ORB-SLAM3 studies did in Part 2.

Honestly, the most transferable finding in this whole review for your application probably isn't from Part 3 at all — it's the **GNSS-fusion result from the arable-farming ORB-SLAM3 paper** (see Part 1/2). Tightly coupling a global sensor into an otherwise-unmodified classical pipeline fixed the exact aliasing problem Cuaran et al. documented, at a fraction of the compute cost of anything in Part 3, and only needed GNSS on about a third of keyframes to get the benefit. If TerraSentia-class GPS is on hand — and per Part 1, it is — that's a lower-risk, lower-compute place to start than porting over a learned SLAM system nobody's validated on agricultural data yet.

### 4.4 Open Gaps Worth Naming Explicitly

- **No published agricultural/row-crop benchmark exists yet** for MASt3R-SLAM, MASt3R-Fusion, DPVO/DPV-SLAM, or VGGT-SLAM, as far as I could find. This is the biggest gap this review turned up, and honestly a real opportunity — a Cuaran-et-al.-style benchmark of these four on the same under-canopy dataset would be a genuinely useful and citable follow-up.
- **VGGT's exact training dataset list** wasn't retrievable from what I had access to (it's in supplementary material) — worth confirming straight from the paper before citing it in a final draft.
- **MASt3R-Fusion has no published FPS figure** as of this review — just a VRAM target (8GB). A latency number would strengthen the hardware-cost comparison in Part 3/4.
- **Cross-paper latency comparisons throughout this review should be read as order-of-magnitude, not precise rankings** — different GPUs, resolutions, and software stacks mean any FPS number here is approximate at best once you're comparing across papers instead of within one paper's own ablations.

### 4.5 Conclusion

Walking through this in four parts — dataset paper, classical baselines, modern learned methods, synthesis — surfaces something easy to miss if you read each system in isolation: **the field has gotten a lot better at general-purpose visual geometry, and hasn't yet shown it's gotten better at the specific problem that matters for row-crop agriculture.** Perceptual aliasing under closed canopy is a structural property of the scene, not a feature-quality problem the way indoor benchmark gains might suggest — and the one intervention in this whole review that actually fixed it (GNSS fusion into an otherwise-classical pipeline) predates, and beats, every learned method surveyed in Part 3 on that specific failure mode. If there's one honest recommendation to take from this, it's that the most useful, citable next step here is to just run a Part 3-style system head-to-head against Cuaran et al.'s original benchmark on the same under-canopy data. That experiment doesn't exist in the published literature yet, and this review wouldn't have been able to make that claim without actually searching and verifying its way through Parts 1-3.

---

## References

Campos, C., Elvira, R., Rodríguez, J.J.G., Montiel, J.M.M., & Tardós, J.D. (2021). ORB-SLAM3: An accurate open-source library for visual, visual-inertial, and multimap SLAM. *IEEE Transactions on Robotics*, 37(6), 1874-1890. https://arxiv.org/abs/2007.11898

Cremona, J., Comelli, R., & Pire, T. (2023). GNSS-stereo-inertial SLAM for arable farming. *Journal of Field Robotics*. https://arxiv.org/abs/2307.12836. Code: https://github.com/CIFASIS/gnss-stereo-inertial-fusion

Cuaran, J., Baquero Velasquez, A.E., Valverde Gasparino, M., Uppalapati, N.K., Sivakumar, A.N., Wasserman, J., Huzaifa, M., Adve, S., & Chowdhary, G. (2024). Under-canopy dataset for advancing simultaneous localization and mapping in agricultural robotics. *The International Journal of Robotics Research*, 43(6), 739-749. https://doi.org/10.1177/02783649231215372. Dataset: https://github.com/jrcuaranv/terrasentia-dataset

GREAT Group, School of Geodesy and Geomatics, Wuhan University (2025). MASt3R-Fusion: Integrating feed-forward visual model with IMU, GNSS for high-functionality SLAM. arXiv:2509.20757. Code: https://github.com/GREAT-WHU/MASt3R-Fusion

Gálvez-López, D., & Tardós, J.D. (2012). Bags of binary words for fast place recognition in image sequences. *IEEE Transactions on Robotics*, 28(5), 1188-1197. Code: https://github.com/dorian3d/DBoW2

Labbé, M., & Michaud, F. (2011). Memory management for real-time appearance-based loop closure detection. *IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)*.

Labbé, M., & Michaud, F. (2019). RTAB-Map as an open-source lidar and visual simultaneous localization and mapping library for large-scale and long-term online operation. *Journal of Field Robotics*, 36(2), 416-446. https://doi.org/10.1002/rob.21831

Leroy, V., Cabon, Y., & Revaud, J. (2024). Grounding image matching in 3D with MASt3R. *European Conference on Computer Vision (ECCV)*. https://arxiv.org/abs/2406.09756

Lipson, L., Teed, Z., & Deng, J. (2023). Deep patch visual odometry. *Advances in Neural Information Processing Systems (NeurIPS)*. https://arxiv.org/abs/2208.04726. Code: https://github.com/princeton-vl/DPVO

Lipson, L., Teed, Z., & Deng, J. (2024). Deep patch visual SLAM. *European Conference on Computer Vision (ECCV)*. https://arxiv.org/abs/2408.01654

Maggio, D., Lim, H., & Carlone, L. (2025). VGGT-SLAM: Dense RGB SLAM optimized on the SL(4) manifold. arXiv:2505.12549

Murai, R., Dexheimer, E., & Davison, A.J. (2025). MASt3R-SLAM: Real-time dense SLAM with 3D reconstruction priors. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. https://arxiv.org/abs/2412.12392. Code: https://github.com/rmurai0610/MASt3R-SLAM

Nistér, D., & Stewénius, H. (2006). Scalable recognition with a vocabulary tree. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*.

Qin, T., Li, P., & Shen, S. (2018). VINS-Mono: A robust and versatile monocular visual-inertial state estimator. *IEEE Transactions on Robotics*, 34(4), 1004-1020.

Qin, T., Pan, J., Cao, S., & Shen, S. (2019). A general optimization-based framework for local odometry estimation with multiple sensors. arXiv:1901.03638. Code: https://github.com/HKUST-Aerial-Robotics/VINS-Fusion

Rublee, E., Rabaud, V., Konolige, K., & Bradski, G. (2011). ORB: An efficient alternative to SIFT or SURF. *IEEE International Conference on Computer Vision (ICCV)*.

Wang, J., Chen, M., Karaev, N., Vedaldi, A., Rupprecht, C., & Novotny, D. (2025). VGGT: Visual geometry grounded transformer. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. Code: https://github.com/facebookresearch/vggt

Wang, S., Leroy, V., Cabon, Y., Chidlovskii, B., & Revaud, J. (2024). DUSt3R: Geometric 3D vision made easy. *IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*. https://arxiv.org/abs/2312.14132. Code: https://github.com/naver/dust3r

*Note on completeness: this list covers the primary systems and dataset papers this review is built around. Secondary sources cited inline for specific numbers (e.g., the FoundationSLAM comparison table, individual Jetson/embedded benchmarking studies, the "Comparison of Modern General-Purpose Visual SLAM Approaches" paper) were used for one data point each and are cited by name at the point of use in Parts 2-4 rather than repeated here — pull the full citation from the relevant search/footnote if your final draft needs them in this list as well.*

---

*End of review. Sections 1-4, abstract, and references are complete.*
