# Geomorphology MCP Server

**Category**: Aesthetic Domain Brick  
**Version**: 1.0.0 (Phase 2.7 + Tier 4D)  
**Architecture**: Three-layer olog  
**Cost Model**: 0 tokens Layers 1–2, creative synthesis at Layer 3

## Overview

Landform process and terrain composition at landscape scale — fluvial valleys, glacial cirques, volcanic cones, coastal cliffs, karst towers, aeolian dunes, and more. Maps the characteristic forms created by each geological agent into deterministic visual vocabularies drawn from physical geography, geomorphology, and Earth science.

**Scale complement**: Operates at the geographic-to-continental range of `powers-of-ten-mcp` (10² to 10⁷ m).  
**Process complement**: Same erosion physics as `patina-weathering-mcp` but at landscape scale rather than material/object scale.

```
Patina & Weathering (material scale) ←→ Geomorphology (landscape scale)
Powers of Ten (all scales)             ←→ Geomorphology (geographic-continental)
```

## Domain Taxonomy

### 8 Landform Processes

| Process | Agent | Time Scale |
|---|---|---|
| Fluvial | Running water | Thousands to millions of years |
| Glacial | Moving ice | Thousands to hundreds of thousands |
| Coastal | Waves, tides, currents | Years to thousands |
| Aeolian | Wind | Years to millions |
| Volcanic | Magma, lava, pyroclastics | Hours to millions |
| Tectonic | Plate movement, faulting | Millions to hundreds of millions |
| Karst | Chemical dissolution | Thousands to millions |
| Mass Wasting | Gravity | Seconds to millennia |

Each process includes erosion features, depositional features, time scale, and visual character.

### 10 Terrain Types

| Terrain | Process | Character |
|---|---|---|
| River Valley | fluvial | Sinuous, terraced, dendritic branching |
| Glacial Cirque | glacial | Amphitheatre curves, knife-edge ridges |
| Volcanic Cone | volcanic | Conical symmetry, radial drainage |
| Sea Cliff | coastal | Vertical planes, progressive retreat |
| Sand Dune | aeolian | Flowing curves, sharp crests, wind-aligned |
| Karst Tower | karst | Extreme vertical, clustered towers |
| Alluvial Plain | fluvial | Extreme horizontal, distributary branching |
| Desert Mesa | aeolian + mass_wasting | Horizontal layers, vertical faces, isolation |
| Barrier Beach | coastal | Linear, narrow, sheltering lagoon |
| Loess Plateau | aeolian | Deeply dissected, vertical faces in soft material |

Each terrain includes 5 visual markers, color palette, and structural character.

### 5 Erosion Intensities

Pristine · Youthful · Mature · Old Age · Peneplain

### 5D Parameter Space

| Parameter | Range | Meaning |
|---|---|---|
| `relief_intensity` | 0–1 | Flat peneplain → extreme vertical relief |
| `erosion_maturity` | 0–1 | Pristine/fresh → deeply weathered/old age |
| `process_energy` | 0–1 | Passive/dormant → actively eroding/depositing |
| `structural_order` | 0–1 | Chaotic mass wasting → highly ordered/geometric |
| `water_presence` | 0–1 | Arid/dry → saturated/submerged |

### 6 Visual Types

`sculptured_vertical` · `flowing_depositional` · `wave_carved` · `wind_sculpted` · `dissolved_karst` · `chaotic_collapse`

## Phase 2.6 — Rhythmic Presets

| Preset | Period | States | Pattern | Role |
|---|---|---|---|---|
| `erosion_cycle` | 16 | river_valley ↔ glacial_cirque | sinusoidal | Shared patina/grading/botanical/scale |
| `coastal_breathing` | 18 | sea_cliff ↔ barrier_beach | sinusoidal | Shared nuclear/splash/patina/grading/botanical/scale |
| `weathering_drift` | 22 | karst_tower ↔ desert_mesa | sinusoidal | Shared catastrophe/heraldic/splash/grading/botanical/scale |
| `aeolian_pendulum` | 24 | sand_dune ↔ loess_plateau | sinusoidal | Shared patina/grading/botanical/scale |
| `tectonic_pulse` | 30 | alluvial_plain ↔ volcanic_cone | sinusoidal | **LCM hub** full-system sync |

## Phase 2.7 — Attractor Presets

| Preset | Basin | Class | Character |
|---|---|---|---|
| `period_30` | 11.6% | lcm_sync | Mature fluvial landscape — most common on Earth |
| `period_29` | 8.4% | lcm_sync | Coastal-fluvial transition — estuary dynamics |
| `period_19` | 7.4% | novel | Glacial-periglacial boundary — edge of ice |
| `period_28` | 2.4% | novel | Volcanic + fluvial tension — creation meets destruction |
| `period_60` | 4.0% | harmonic | Full geomorphic repertoire long cycle |
| `bifurcation_edge` | — | curated | Erosion/deposition threshold — graded equilibrium |
| `organic_complexity` | — | curated | Karst cathedral — maximum landscape complexity |

## Tool Catalog (21 tools)

### Layer 1 — Pure Taxonomy (0 tokens)

| Tool | Purpose |
|---|---|
| `list_landform_processes` | All 8 processes with agents and features |
| `get_landform_process_details` | Full spec for one process |
| `list_terrain_types` | All 10 terrain types |
| `get_terrain_type_details` | Full spec with visual markers and palette |
| `list_erosion_intensities` | 5 erosion intensity grades |
| `get_geomorph_canonical_states` | 10 canonical states with 5D coords |
| `get_geomorph_visual_types` | 6 visual types with keywords + optical |

### Layer 2 — Deterministic Mapping (0 tokens)

| Tool | Purpose |
|---|---|
| `classify_geomorph_intent` | Intent → terrain + process |
| `map_geomorph_parameters` | Terrain → visual parameters + vocabulary |
| `list_geomorph_rhythmic_presets` | 5 Phase 2.6 preset catalog |
| `apply_geomorph_rhythmic_preset` | Generate full oscillation sequence |
| `generate_geomorph_rhythmic_sequence` | Custom oscillation between any two states |
| `compute_geomorph_distance` | 5D Euclidean distance between states |
| `compute_geomorph_trajectory` | Smooth morphospace trajectory |
| `extract_geomorph_visual_vocabulary` | Coords → image-gen keywords + optical |
| `list_geomorph_attractor_presets` | 7 Phase 2.7 attractor catalog |
| `generate_geomorph_attractor_prompt` | Attractor → composite/split/sequence prompt |
| `generate_geomorph_sequence_prompts` | Rhythmic preset → keyframe prompts |

### Layer 3 — Claude Synthesis Interface

| Tool | Purpose |
|---|---|
| `enhance_geomorph_prompt` | Full enhancement package for Claude composition |

### Utility

| Tool | Purpose |
|---|---|
| `get_geomorph_domain_registry_config` | Tier 4D integration data |
| `get_server_info` | Server metadata and capabilities |

## Deployment

### FastMCP Cloud

```bash
fastmcp deploy geomorphology_mcp.py:mcp
```

### Local

```bash
pip install fastmcp
python geomorphology_mcp.py
```

## Functorial Connections

- **Geomorph × Patina Weathering**: Same erosion physics at different scales — rust on iron vs canyon in sandstone
- **Geomorph × Powers of Ten**: Geomorphology occupies the geographic-to-continental scale band
- **Geomorph × Botanical Growth**: Vegetation stabilizes slopes, roots break rock, succession follows erosion
- **Geomorph × Splash Aesthetics**: Fluvial and coastal processes ARE water dynamics at landscape scale
- **Geomorph × Stage Lighting**: Raking light across terrain relief is fundamental landscape photography
- **Geomorph × Film Color Grading**: Desert warm, glacial cool, coastal neutral — terrain implies colour palette

## Compatible Servers

`patina-weathering-mcp` · `powers-of-ten-mcp` · `botanical-growth-stages-mcp` · `film-color-grading-mcp` · `stage-lighting-mcp` · `splash-aesthetics-mcp` · `catastrophe-morph-mcp` · `surface-design-aesthetics` · `microscopy-aesthetics-mcp` · `aesthetic-dynamics-core` · `composition-graph-mcp`

## Science Foundation

Fluvial geomorphology (Hjulström curve, stream power) · Glacial geology (cirque erosion, till deposition) · Coastal processes (wave refraction, longshore drift) · Aeolian geomorphology (saltation, dune migration) · Volcanology (effusive vs explosive, cone morphology) · Structural geology (faulting, folding, plate tectonics) · Karst science (dissolution kinetics, speleogenesis) · Davis cycle of erosion (youth, maturity, old age, peneplain)
