# Patina & Weathering MCP Server

**Category**: Aesthetic Domain Brick  
**Version**: 1.0.0 (Phase 2.7 + Tier 4D)  
**Architecture**: Three-layer olog  
**Cost Model**: 0 tokens Layers 1–2, creative synthesis at Layer 3

## Overview

Conservation-science weathering composition that adds a **temporal decay/aging axis** to every material domain in the Lushy ecosystem. Maps the full lifecycle of physical materials — from factory-fresh to archaeological ruin — using deterministic taxonomies drawn from conservation science, materials engineering, geological weathering, and wabi-sabi aesthetic philosophy.

This is the ecosystem's primary **Temporal/Entropy** domain, filling the largest single gap identified in the Feb 2026 compositional dynamics analysis.

## What It Covers

| Gap Filled | How |
|---|---|
| **Temporal/Entropy** | 8 canonical states spanning pristine → ruin, with continuous interpolation |
| **Accumulation/Accretion** | Biological colonization progression, efflorescence bloom, oxide layering |
| **Palimpsest** | Multi-layer visual vocabulary — paint ghosts, repair evidence, archaeological strata |

## Domain Taxonomy

### 11 Material Categories
Ferrous metals (rust) · Copper alloys (verdigris) · Silver (tarnish) · Limestone & marble (dissolution) · Sandstone (tafoni, desert varnish) · Wood (silvering, checking) · Ceramics & glazes (craquelure) · Paper & textiles (foxing, yellowing) · Paint & coatings (alligatoring, peeling) · Concrete (spalling, efflorescence) · Glass (devitrification, iridescence)

### 6 Weathering Agents
Water · UV/Solar · Chemical · Biological · Mechanical · Thermal

### 6 Conservation Condition Grades
Pristine → Light weathering → Moderate weathering → Advanced decay → Severe deterioration → Ruin

### 5D Parameter Space
| Parameter | Range | Meaning |
|---|---|---|
| `exposure_duration` | 0–1 | Freshly made → geological time |
| `agent_intensity` | 0–1 | Sheltered → extreme environmental attack |
| `material_resistance` | 0–1 | Fragile (paper) → hard (granite, bronze) |
| `intervention_state` | 0–1 | Untouched → heavily conserved/restored |
| `aesthetic_character` | 0–1 | Ugly destructive decay → noble wabi-sabi patina |

### 8 Canonical States
`fresh_pristine` · `gentle_patina` · `noble_verdigris` · `deep_rust` · `stone_erosion` · `paper_foxing` · `cracked_glaze` · `total_ruin`

### 6 Visual Types
`pristine_surface` · `warm_aged` · `oxidation_bloom` · `erosion_sculpted` · `fracture_network` · `archaeological_layer`

## Phase 2.6 — Rhythmic Presets

Five curated oscillation patterns for temporal composition:

| Preset | Period | States | Pattern | Role |
|---|---|---|---|---|
| `aging_cycle` | 16 | pristine ↔ deep_rust | triangular | Unique gap-filler 15–17 |
| `erosion_pulse` | 18 | stone_erosion ↔ gentle_patina | sinusoidal | Shared nuclear/catastrophe/diatom/splash |
| `restoration_pendulum` | 20 | total_ruin ↔ gentle_patina | sinusoidal | Common period 20 |
| `oxidation_bloom` | 24 | pristine ↔ noble_verdigris | sinusoidal | Near catastrophe/diatom |
| `entropy_wave` | 30 | gentle_patina ↔ total_ruin | sinusoidal | **LCM hub** full-system sync |

## Phase 2.7 — Attractor Presets

Seven discovered/curated attractor presets for multi-domain prompt generation:

| Preset | Basin | Class | Character |
|---|---|---|---|
| `period_30` | 11.6% | lcm_sync | Warm-aged antique — gentle time-enriched character |
| `period_29` | 8.4% | lcm_sync | Mid-aged stone with lichen — emergent composite |
| `period_19` | 7.4% | novel | Cuprite → verdigris transition boundary |
| `period_28` | 2.4% | novel | Craquelure tension — beautiful pattern as deterioration |
| `period_60` | 4.0% | harmonic | Full weathering repertoire long cycle |
| `bifurcation_edge` | — | curated | Patina ↔ decay conservation threshold |
| `organic_complexity` | — | curated | Wabi-sabi perfection — maximum beauty from age |

## Tool Catalog (21 tools)

### Layer 1 — Pure Taxonomy (0 tokens)
| Tool | Purpose |
|---|---|
| `list_material_categories` | All 11 material categories |
| `get_material_details` | Full spec for one material |
| `list_weathering_agents` | All 6 agent categories |
| `get_weathering_agent_details` | Full spec for one agent |
| `list_condition_grades` | Conservation 6-grade scale |
| `get_patina_canonical_states` | 8 canonical states with 5D coords |
| `get_patina_visual_types` | 6 visual types with keywords + optical |

### Layer 2 — Deterministic Mapping (0 tokens)
| Tool | Purpose |
|---|---|
| `classify_weathering_intent` | Intent → material + agent + condition + aesthetic |
| `map_weathering_parameters` | Specification → visual parameters + vocabulary |
| `list_patina_rhythmic_presets` | 5 Phase 2.6 preset catalog |
| `apply_patina_rhythmic_preset` | Generate full oscillation sequence |
| `generate_patina_rhythmic_sequence` | Custom oscillation between any two states |
| `compute_patina_distance` | 5D Euclidean distance between states |
| `compute_patina_trajectory` | Smooth morphospace trajectory |
| `extract_patina_visual_vocabulary` | Coords → image-gen keywords + optical |
| `list_patina_attractor_presets` | 7 Phase 2.7 attractor catalog |
| `generate_patina_attractor_prompt` | Attractor → composite/split/sequence prompt |
| `generate_patina_sequence_prompts` | Rhythmic preset → keyframe prompts |

### Layer 3 — Claude Synthesis Interface
| Tool | Purpose |
|---|---|
| `enhance_patina_prompt` | Full enhancement package for Claude composition |

### Utility
| Tool | Purpose |
|---|---|
| `get_patina_domain_registry_config` | Tier 4D integration data |
| `get_server_info` | Server metadata and capabilities |

## Deployment

### FastMCP Cloud

```bash
fastmcp deploy patina_weathering_mcp.py:mcp
```

### Local

```bash
pip install fastmcp
python patina_weathering_mcp.py
```

### Entrypoint

```
patina_weathering_mcp.py:mcp
```

## Usage Workflow

```
1. classify_weathering_intent("old copper dome with green streaks")
   → material: copper_alloy, agent: water, condition: moderate_weathering

2. map_weathering_parameters(material_id="copper_alloy", condition_grade="moderate_weathering")
   → visual type, vocabulary, optical properties, color stage

3. enhance_patina_prompt(user_intent="...", intensity="dramatic")
   → complete structured data for Claude to synthesize final prompt
```

## Functorial Connections

- **Material base → surface design domains**: temporal transform (any material × any age)
- **Condition grade → catastrophe theory**: phase transitions at degradation thresholds
- **Biological colonization → diatom/microscopy**: lichen, moss, algae as visual texture
- **Color transformation → stage lighting**: oxide colours under different illumination
- **Structural integrity → splash dynamics**: crack propagation, spalling mechanics

## Compatible Servers

`catastrophe-morph-mcp` · `diatom-morphology-mcp` · `surface-design-aesthetics` · `microscopy-aesthetics-mcp` · `stage-lighting-mcp` · `splash-aesthetics-mcp` · `aesthetic-dynamics-core` · `composition-graph-mcp`

## Science Foundation

Conservation science condition assessment · Materials engineering degradation mechanisms · Geological weathering processes · Archaeological stratigraphy · Wabi-sabi aesthetic philosophy
