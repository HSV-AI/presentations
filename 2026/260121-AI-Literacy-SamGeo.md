![HSV-AI Logo](https://hsv.ai/wp-content/uploads/2022/03/logo_v11_2022.png)

# AI Literacy


---


# SamGeo 3: Next-Generation Geospatial Segmentation
**Date:** January 21, 2026  
**Audience:** Developers & AI Practitioners

---

## 1. Overview
**SamGeo 3** is a specialized extension of the `segment-geospatial` ecosystem, integrating Meta’s **Segment Anything Model 3 (SAM 3)**. It bridges the gap between foundation vision models and Geographic Information Systems (GIS), allowing for zero-shot feature extraction from satellite, aerial, and drone imagery.

## 2. Primary Capabilities

### 🛰️ Multi-Modal Prompting
Extract features using various inputs without retraining:
1. **Text Prompts:** Identify features by name (e.g., "blue swimming pools", "shipping containers").
2. **Point & Box Prompts:** Manually guide the model by clicking on objects or drawing bounding boxes.
3. **Interactive Refinement:** Add or remove points to fine-tune masks in real-time.



### 🗺️ Vector-Ready Outputs
Automatically convert raster masks into industry-standard geospatial formats:
* **Formats:** GeoTIFF, GeoPackage, Shapefile, and GeoJSON.
* **CRS Handling:** Automatic projection and coordinate system management for seamless integration into QGIS or ArcGIS.

### 📽️ Temporal & Video Analytics
Leveraging the SAM 3 architecture, SamGeo 3 can now track objects across a sequence of satellite images or drone footage, maintaining object ID consistency even during brief occlusions.

### ⚡ Zero-Shot Generalization
The model performs exceptionally well on diverse terrains (urban, rural, desert, forest) without requiring local training data or manual labeling.

---

## 3. Installation & Setup

For the most stable experience, it is recommended to use a Python 3.12 environment.

### Standard Installation
```bash
pip install -U "segment-geospatial[samgeo3]"
```

## 4. Developer Guidance
Model Initialization
When initializing the model class, developers should specify the backend and interactivity settings:

```python

from samgeo import SamGeo3

sam = SamGeo3(
    model_type="vit_h",      # Choices: vit_h, vit_l, vit_b
    checkpoint="sam3.pth", 
    enable_inst_interactivity=True
)
```

Best Practices for AI Practitioners
Hybrid Workflows: Combine text prompts for initial broad detection with box exemplars to refine precision.

Presence Scores: Utilize the output "presence score" to automate quality control—discarding low-confidence masks in large-scale pipelines.

Memory Management: For high-resolution satellite tiles, use the built-in tile_segmentation method to avoid GPU OOM (Out of Memory) errors.

## 5. Resources & Documentation

Source Code: GitHub - [opengeos/segment-geospatial](https://samgeo.gishub.org/)

Jupyter Notebook - https://samgeo.gishub.org/examples/input_prompts/
