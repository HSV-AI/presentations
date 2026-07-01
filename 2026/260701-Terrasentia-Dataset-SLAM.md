---
marp: true
theme: default
paginate: true
size: 16:9
---

<!-- _class: lead -->

![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# Under the Canopy: The TerraSentia Dataset for Agricultural SLAM

**Date:** July 1, 2026
**Audience:** Robotics & AI Practitioners

**Note:** To present this with Marp, use: `npx @marp-team/marp-cli --allow-local-files 260701-Terrasentia-Dataset-SLAM.md -o slides.html`

---

## **1 Why This Is Hard: SLAM Under the Canopy (1/2)**

Visual SLAM (Simultaneous Localization And Mapping) is mature for indoor and urban robots, but agriculture breaks most of the usual assumptions.

* **No GPS to lean on:** under a corn canopy, satellite signal is heavily attenuated — localization has to come mostly from cameras, IMU, and wheel odometry.
* **Repetitive structure:** every corn row looks like every other corn row. Loop closure (recognizing "I've been here before") is prone to false matches.
* **Moving, textureless "obstacles":** leaves sway in the wind and create constantly-changing occlusions and unreliable visual features.

---

## **1 Why This Is Hard: SLAM Under the Canopy (2/2)**

* **Rough terrain:** tilled soil and row ruts vibrate the camera and add high-frequency noise to inertial measurements.
* **Growth-stage & seasonal drift:** the same field looks completely different in June vs. September — a model tuned on one pass may fail on the next.

---

![bg right:40% width:100%](figures/robot.png)

## The Gap This Dataset Fills

Prior agricultural datasets (Rosario, sugar-beet/BoniRob, tractor-mowing) each cover only a slice of these challenges — over-canopy only, low frame rate, or a single collection day.

TerraSentia was built to cover **all of it at once**: under-canopy, multi-month, multi-crop, high frame rate.

---

## **2 The Dataset: Overview**

* **Robot platform:** TerraSentia — 4-wheel skid-steering ground robot, Jetson AGX Orin compute, PCIe 4.0 SSD storage.
* **Collection site:** Illinois Autonomous Farm, University of Illinois Urbana-Champaign, June–September 2022.
* **Scale:** 135 sequences, **1,060 GB total**, **9.7 hours** of video.

---

## **2 The Dataset: Sensor Suite**

| Sensor | Detail |
|---|---|
| Stereo-inertial camera | ZED2 (StereoLabs), 120° FOV, built-in IMU @ 200 Hz |
| Rosbag images | 832×468 px, 30 fps (small, ready for V-SLAM) |
| SVO images | 1280×720 px, H.265 @ ~100:1 compression |
| Robot IMU | 6 DOF, 86 Hz |
| GPS | Standard + RTK (20% of sequences, <2 cm accuracy) |
| Wheel encoders | wheel radius 0.086 m, track width 0.26 m / 0.29 m |

---

## **2 The Dataset: Crop Coverage — Corn**

| Folder | Sequences | Span | Weeds | Weather var. | Growth-stage var. | Size (GB) |
|---|---|---|---|---|---|---|
| Cornfield 1 | 80 | 4 months | ✓ | ✓ | ✓ | 584 |
| Cornfield 2 | 17 | 3 months | ✓ | ✓ | ✓ | 171 |
| Cornfield 3 | 2 | 1 week | x | x | x | 28 |
| Cornfield 4 | 4 | 1 month | ✓ | x | ✓ | 37 |

---

## **2 The Dataset: Crop Coverage — Other Crops & Corridors**

| Folder | Sequences | Span | Weeds | Weather var. | Growth-stage var. | Size (GB) |
|---|---|---|---|---|---|---|
| Sorghum | 2 | 3 weeks | ✓ | x | x | 9 |
| Soybean | 12 | 2 weeks | ✓ | ✓ | x | 79 |
| Sweet corn | 4 | 1 week | ✓ | x | x | 49 |
| Others (corridors, campus) | 14 | 3 months | x | ✓ | ✓ | 103 |

---

## **2 The Dataset: Two File Formats, Two Purposes**

| | **Rosbag (.bag)** | **SVO (.svo)** |
|---|---|---|
| Contents | All sensors: stereo, IMU, GPS, wheel encoders, EKF ground truth, ZED VIO/VI-SLAM topics | Stereo images + metadata only |
| Resolution | 832×468 | 1280×720 |
| Best for | Full multi-sensor SLAM development | High-res imagery / high-quality neural depth |
| Tooling | ROS, or pip-installable `rosbags` | Stereolabs ZED SDK (needs CUDA + matching GPU driver) |

---

![bg right:40% width:100%](figures/coordinate_frames.png)

## Sensor Coordinate Frames

Camera intrinsics, extrinsics between sensors, and IMU noise parameters were all estimated with the Kalibr calibration tool — full values are in `sensor_parameters.txt`.

---

## **3 How to Use It: A Field Report**

Two extraction paths exist depending on which file format you're after.

**Path A — Rosbag** (recommended if you don't want to install full ROS)
**Path B — SVO** (higher-res imagery, needs the ZED SDK)

---

## **3 Field Report: Path A — Rosbag**

* Use the pip-installable `rosbags` library instead of a catkin workspace.
* Gotchas hit along the way:
  * `conn.msgdef` is a `MessageDefinition` object in `rosbags` 0.11, not a raw string — need `.data`.
  * Depth encoding isn't consistent across bags — some are `32FC1` (float meters), others `16UC1` (uint16 mm already). Branch on `msg.encoding`.
  * Not every bag has `/terrasentia/full_gps` — guard downstream GPS parsing/plotting for the empty case.

---

## **3 Field Report: Path B — SVO (Setup)**

* Requires the Stereolabs ZED SDK matched to your **CUDA version** — the newer SDK versions gate the download behind a form.
* Had to fall back from Python 3.12 → **3.10**, then manually install the `pyzed` wheel produced by the system ZED installer into the venv (ZED isn't on PyPI).

---

## **3 Field Report: Path B — SVO (Calibration & Output)**

* Neural-depth calibration hung, stalling around 90% optimization — worked around it:
  ```python
  init_params.camera_disable_self_calib = True
  init_params.depth_mode = sl.DEPTH_MODE.NONE
  ```
* Output is per-frame PNGs (left/right) + a pose file — stitched into video with `ffmpeg`.

**Bottom line:** for most SLAM/VO development, the Rosbag + `rosbags` path is far less friction than SVO + the ZED SDK.

---

![bg right:40% width:100%](figures/neural_depth.png)

## **4 Demo**

* Extracted video from a Cornfield1 rosbag (`ts_2022_08_10_10h29m14s_four_rows`) — visibly choppy/rough footage that makes clear why under-canopy navigation is hard.
* GPS track plot (`view_gps_graph.py`) for a sequence with recorded `/terrasentia/full_gps`.
* *(Live: play the extracted clips and walk through the GPS plot.)*

---

## **5 Core Concepts You Need Going In**

* **VO vs. V-SLAM**
  * **Visual Odometry (VO):** estimates ego-motion frame-to-frame — drifts over time, no memory of the past.
  * **Visual SLAM (V-SLAM):** VO + **loop closure** — recognizes revisited places and globally corrects accumulated drift.
* **Direct vs. indirect methods**
  * **Direct:** match frames using raw pixel intensities (photometric error).
  * **Indirect:** detect and match sparse features, minimizing reprojection error.

---

## **5 Core Concepts: Estimation Approaches**

* **Filter-based vs. optimization-based**
  * **Filter-based** (e.g. MSCKF, OpenVINS): propagate a state vector (poses + landmarks) through predict/update steps — cheap, but bounded memory.
  * **Optimization-based** (e.g. ORB-SLAM3, VINS-Fusion): bundle adjustment / factor-graph optimization over keyframes — more accurate, more compute.

---

## **5 Core Concepts: Ground Truth & Metrics**

* **Ground truth without a perfect GPS:** RTK GPS alone doesn't give orientation, so the authors fused GPS + control commands with an **Extended Kalman Filter (EKF)** and a **Moving Horizon Estimator (MHE)** to produce a usable ground-truth trajectory.
* **How accuracy is scored**
  * **ATE (Absolute Trajectory Error):** global consistency.
  * **RPE (Relative Pose Error):** local drift per meter traveled.

---

## **6 Benchmark Results: How Well Does SLAM Actually Do Here?**

Systems tested: **ORB-SLAM3, VINS-Fusion, SVO Pro, RTAB-Map, OpenVINS, MSCKF, ZED odometry** — across 4 scenarios of increasing difficulty (semi-structured double-loop → corridor → early-growth rows → late-growth rows).

* **Scenario 1 (easiest, semi-structured):** every system closes the loop; ATE under 1.2 m. VINS-Fusion best overall.
* **Scenario 2 (repetitive corn/soybean corridor):** only VINS-Fusion reliably closes the loop — repetitive rows fool bag-of-words place recognition. ATE balloons up to **7.3 m**.

---

## **6 Benchmark Results, Continued**

* **Scenario 3 (early-growth rows, rough soil, moving leaves):** RTAB-Map and ORB-SLAM3 lose tracking mid-row; VIO-only systems (no loop closure needed) hold up better, drift under 0.4 m.
* **Scenario 4 (late-growth, heavy occlusion):** RTAB-Map and ORB-SLAM3 **fail completely**. Even ZED's onboard odometry blows out to 27.7 m ATE. Only VIO methods with loop closure disabled make it through.

**Takeaway:** the same algorithms that get centimeter-level accuracy indoors can drift by *meters* under a canopy — right around the spacing between plants. That gap is exactly why this dataset matters for anyone building ag robotics perception.

---

## **References & Resources: Paper & Dataset**

* **Paper:** [Cuaran et al., "Under-canopy dataset for advancing simultaneous localization and mapping in agricultural robotics," IJRR 2023](https://journals.sagepub.com/doi/abs/10.1177/02783649231215372)
* **Dataset download:** [Box — Terrasentia dataset](https://uofi.box.com/s/l7e0okjxkq1vzz77goac2bu1my81ad9d)
* **Supplementary material:** [Box — Paper supplement](https://uofi.box.com/s/cns333ty3t04lib5mjnq16tycxokztp2)
* **GitHub repo (download scripts):** [jrcuaranv/terrasentia-dataset](https://github.com/jrcuaranv/terrasentia-dataset)

---

## **References & Resources: Tools & Systems**

### **Tools Used in This Talk**

* **ZED SDK:** [stereolabs.com/developers/release](https://www.stereolabs.com/developers/release/)
* **rosbags (pure-Python ROS bag reader):** [PyPI - rosbags](https://pypi.org/project/rosbags/)
* **Kalibr (sensor calibration tool used by the authors):** [ethz-asl/kalibr](https://github.com/ethz-asl/kalibr)

### **SLAM Systems Benchmarked in the Paper**

* ORB-SLAM3, VINS-Fusion, SVO Pro, RTAB-Map, OpenVINS, MSCKF, ZED odometry
