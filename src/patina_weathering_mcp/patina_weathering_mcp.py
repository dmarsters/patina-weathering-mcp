"""
Patina & Weathering MCP Server

Three-layer architecture for zero-cost weathering aesthetic composition:
- Layer 1: Pure taxonomy (materials, agents, weathering types, decay patterns)
- Layer 2: Deterministic mapping (intent → parameters, classification, vocabulary)
- Layer 3: Claude synthesis interface

Phase 2.6: Rhythmic presets with 5 curated oscillation patterns
    - aging_cycle (16):            pristine ↔ deep_rust (unique gap-filler 15-17)
    - restoration_pendulum (20):   total_ruin ↔ gentle_patina (shared with common period 20)
    - oxidation_bloom (24):        fresh_pristine ↔ noble_verdigris (shared near catastrophe/diatom)
    - erosion_pulse (18):          stone_erosion ↔ gentle_patina (shared with nuclear/catastrophe/diatom/splash)
    - entropy_wave (30):           gentle_patina ↔ total_ruin (LCM hub)

Phase 2.7: Attractor visualization prompt generation
    - 7 discovered/curated attractor presets from Tier 4D analysis
    - Composite, split-view, and sequence prompt modes
    - Domain registry helper for emergent attractor discovery

Based on conservation science, materials engineering, and wabi-sabi aesthetics.
"""

from fastmcp import FastMCP
import json
import math
from typing import Dict, List, Any, Optional

# Initialize FastMCP server
mcp = FastMCP("Patina & Weathering")


# ============================================================================
# LAYER 1: MATERIAL TAXONOMY (0 TOKENS)
# ============================================================================

# Material categories with characteristic weathering behaviors
MATERIAL_CATEGORIES = {
    "ferrous_metal": {
        "name": "Ferrous Metals",
        "description": "Iron and steel — rust (iron oxide) is the defining weathering product",
        "examples": ["cast iron", "wrought iron", "mild steel", "weathering steel (Corten)"],
        "primary_weathering": "oxidation",
        "characteristic_patina": "Fe₂O₃ rust — orange-brown to deep red-black",
        "color_progression": ["bare metallic grey", "orange flash rust", "red-brown oxide", "dark brown-black scale", "flaking laminar rust"],
        "time_scale": "weeks to decades",
        "visual_markers": [
            "weeping rust stains below fastener points",
            "laminar scale lifting from substrate in curved plates",
            "pinpoint pitting beneath intact oxide layer",
            "orange-brown tide marks at moisture boundaries",
            "red-black stable magnetite core under flaking hematite"
        ]
    },
    "copper_alloy": {
        "name": "Copper & Bronze",
        "description": "Copper, brass, bronze — verdigris (copper carbonate) is the noble patina",
        "examples": ["copper sheet", "bronze casting", "brass hardware", "phosphor bronze"],
        "primary_weathering": "oxidation_carbonate",
        "characteristic_patina": "Cu₂(OH)₂CO₃ verdigris — green to blue-green",
        "color_progression": ["bright salmon-pink", "dull brown cuprite", "mottled brown-green", "stable green verdigris", "blue-green patina with streaking"],
        "time_scale": "months to centuries",
        "visual_markers": [
            "bright green drip streaks below exposed copper edges",
            "mottled brown-to-green transition zone at sheltered boundary",
            "stable blue-green crust with crystalline surface texture",
            "salmon-pink bright metal visible at rubbed high points",
            "dark brown cuprite underlayer showing through verdigris chips"
        ]
    },
    "silver": {
        "name": "Silver",
        "description": "Sterling and fine silver — tarnish (silver sulfide) darkens progressively",
        "examples": ["sterling silver", "silver plate", "fine silver", "Britannia silver"],
        "primary_weathering": "sulfide_tarnish",
        "characteristic_patina": "Ag₂S tarnish — gold to purple-black",
        "color_progression": ["bright mirror white", "pale gold warmth", "amber-bronze", "deep purple-blue iridescence", "matte charcoal-black"],
        "time_scale": "hours to years",
        "visual_markers": [
            "golden warmth on protected recessed surfaces",
            "iridescent purple-blue in deepest relief areas",
            "bright white rub marks on high-contact edges and peaks",
            "progressive darkening gradient from exposed to sheltered",
            "matte black sulfide in crevices contrasting polished highlights"
        ]
    },
    "limestone": {
        "name": "Limestone & Marble",
        "description": "Calcium carbonate stone — dissolves in acid rain, sugars and spalls",
        "examples": ["Portland limestone", "Carrara marble", "travertine", "chalk", "oolitic limestone"],
        "primary_weathering": "dissolution_biological",
        "characteristic_patina": "rounded edges, biological colonization, black gypsum crust",
        "color_progression": ["clean cream-white", "light grey soiling", "black gypsum crust on sheltered faces", "orange lichen colonization", "deep grey-green biological cover"],
        "time_scale": "years to centuries",
        "visual_markers": [
            "sharp carved edges rounded to soft pillowed forms",
            "black gypsum crust thick on sheltered undersides",
            "clean white stone on rain-washed exposed faces",
            "orange and grey circular lichen colonies on stable surfaces",
            "sugaring surface where individual calcite grains detach"
        ]
    },
    "sandstone": {
        "name": "Sandstone",
        "description": "Cemented quartz grains — weathers by loss of binder, spalling, salt damage",
        "examples": ["red sandstone", "Yorkstone", "brownstone", "Berea sandstone"],
        "primary_weathering": "granular_disaggregation",
        "characteristic_patina": "rounded forms, cavernous hollows, desert varnish",
        "color_progression": ["fresh cut colour (pink/buff/red)", "surface darkening from iron mobilization", "differential erosion revealing bedding", "honeycomb weathering caverns", "desert varnish dark brown-black"],
        "time_scale": "decades to millennia",
        "visual_markers": [
            "honeycomb tafoni cavities eroded by salt crystallization",
            "case-hardened surface shell over soft eroded interior",
            "differential erosion picking out cross-bedding laminae",
            "dark desert varnish manganese-oxide coating on exposed faces",
            "grain-by-grain surface disaggregation leaving sandy residue"
        ]
    },
    "wood": {
        "name": "Wood",
        "description": "Timber — weathers to silver-grey, checks, splits, hosts biological growth",
        "examples": ["oak", "cedar", "pine", "teak", "driftwood"],
        "primary_weathering": "photodegradation_biological",
        "characteristic_patina": "silver-grey photodegraded surface, checking, biological colonization",
        "color_progression": ["fresh-cut heartwood colour", "UV darkening to golden-brown", "grey surface fibre degradation", "silver-grey stable weathered", "deep grey-black with moss/lichen"],
        "time_scale": "months to decades",
        "visual_markers": [
            "end-grain checking radiating from pith center",
            "surface fibre lifting creating rough tactile grain",
            "silver-grey colour uniform across UV-exposed faces",
            "dark staining below iron hardware (tannin reaction)",
            "moss and lichen colonizing shaded damp surfaces"
        ]
    },
    "ceramic_glaze": {
        "name": "Ceramics & Glazes",
        "description": "Fired clay with glass-phase glaze — crazes, spalls, develops craquelure",
        "examples": ["porcelain", "stoneware", "earthenware", "terracotta", "majolica"],
        "primary_weathering": "thermal_mechanical",
        "characteristic_patina": "craquelure network, glaze chips, stained craze lines",
        "color_progression": ["pristine glossy surface", "fine craze network developing", "stained craze lines (tea/dirt penetration)", "glaze chips revealing bisque body", "extensive loss with stabilized fragments"],
        "time_scale": "years to centuries",
        "visual_markers": [
            "fine craquelure network with stained intersections",
            "conchoidal glaze chips exposing pale bisque substrate",
            "crazing pattern denser at glaze pooling and thick spots",
            "salt efflorescence white crystals on unglazed terracotta",
            "iron spot blooming through reduction-fired glaze"
        ]
    },
    "paper_textile": {
        "name": "Paper & Textiles",
        "description": "Organic fibrous materials — fox, yellow, fade, embrittle, tear",
        "examples": ["rag paper", "wood-pulp paper", "vellum", "cotton canvas", "silk", "linen"],
        "primary_weathering": "chemical_photodegradation",
        "characteristic_patina": "foxing spots, yellowing, tide marks, fibre degradation",
        "color_progression": ["bright white/original colour", "warm ivory yellowing", "brown foxing spots scattered", "overall tan-brown tone", "darkened brittle fragments"],
        "time_scale": "years to centuries",
        "visual_markers": [
            "scattered brown foxing spots of varying diameter",
            "tide mark brown ring where moisture boundary dried",
            "overall warm yellowing from acid migration in wood-pulp",
            "fading pattern revealing UV exposure direction",
            "brittle edge crumbling where fibre chains have broken"
        ]
    },
    "paint_coating": {
        "name": "Paint & Coatings",
        "description": "Applied surface films — chalk, alligator, peel, blister, fade",
        "examples": ["oil paint", "latex/acrylic paint", "lacquer", "varnish", "distemper"],
        "primary_weathering": "photodegradation_mechanical",
        "characteristic_patina": "chalking, alligatoring, peeling revealing substrate layers",
        "color_progression": ["fresh glossy saturated colour", "gloss loss and chalking", "fine cracking (checking)", "alligator pattern deep cracking", "curl-edged peeling revealing layers beneath"],
        "time_scale": "years to decades",
        "visual_markers": [
            "chalking powder surface that marks on contact",
            "alligator-pattern deep cracks dividing surface into cells",
            "curl-edged paint flakes lifting from substrate",
            "ghost layer — faded remnant of stripped previous coat",
            "blister domes where moisture trapped under film"
        ]
    },
    "concrete": {
        "name": "Concrete",
        "description": "Portland cement composite — spalls, carbonates, stains from rebar corrosion",
        "examples": ["reinforced concrete", "precast panels", "poured-in-place", "shotcrete"],
        "primary_weathering": "carbonation_corrosion",
        "characteristic_patina": "spalling over rebar, efflorescence, rain-streak staining",
        "color_progression": ["fresh grey with formwork texture", "darkening from moisture absorption", "white efflorescence salt bloom", "rust staining from corroding rebar", "spalling craters with exposed reinforcement"],
        "time_scale": "decades to century",
        "visual_markers": [
            "white efflorescence salt blooms at cracks and joints",
            "rust-brown stain trails below cracks (rebar corrosion indicator)",
            "delamination spalls exposing corroded reinforcing bar",
            "carbonation front visible as pH boundary in cross-section",
            "rain-streak differential soiling creating vertical stripes"
        ]
    },
    "glass": {
        "name": "Glass",
        "description": "Amorphous silicate — devitrifies, weeps, develops iridescence",
        "examples": ["soda-lime glass", "lead glass", "borosilicate", "stained glass"],
        "primary_weathering": "devitrification",
        "characteristic_patina": "iridescent surface layers from ion exchange, weeping, pitting",
        "color_progression": ["clear transparent", "slight haze from surface leaching", "milky opalescence", "iridescent rainbow interference films", "opaque white devitrified crust"],
        "time_scale": "decades to millennia (archaeological)",
        "visual_markers": [
            "iridescent rainbow film from thin-layer interference",
            "surface pitting with concentric ring pattern",
            "weeping droplets from alkali leaching in humid conditions",
            "opaque white devitrified layer on buried archaeological glass",
            "crizzling fine internal crack network from unstable composition"
        ]
    }
}

# Weathering agent taxonomy
WEATHERING_AGENTS = {
    "water": {
        "name": "Water Exposure",
        "mechanisms": ["dissolution", "freeze-thaw cycling", "salt crystallization", "hydration", "erosion"],
        "visual_indicators": ["tide marks", "efflorescence", "spalling", "rounding", "drip staining"],
        "severity_markers": {
            "mild": "occasional rain exposure, sheltered",
            "moderate": "regular wetting-drying cycles",
            "severe": "immersion, coastal salt spray, freeze-thaw"
        }
    },
    "uv_solar": {
        "name": "UV / Solar Radiation",
        "mechanisms": ["photodegradation", "colour fading", "embrittlement", "chalking", "chain scission"],
        "visual_indicators": ["fading pattern", "chalking", "colour shift", "surface fibre degradation", "gloss loss"],
        "severity_markers": {
            "mild": "indoor diffuse light",
            "moderate": "shaded exterior or oriented away from sun",
            "severe": "full southern exposure, high altitude, equatorial"
        }
    },
    "chemical": {
        "name": "Chemical Attack",
        "mechanisms": ["acid rain dissolution", "sulfation", "salt attack", "pollution soiling", "galvanic corrosion"],
        "visual_indicators": ["black gypsum crust", "green copper staining", "rust bleeding", "etching", "efflorescence"],
        "severity_markers": {
            "mild": "rural clean air",
            "moderate": "urban atmosphere",
            "severe": "industrial / coastal / high pollution"
        }
    },
    "biological": {
        "name": "Biological Colonization",
        "mechanisms": ["lichen colonization", "moss growth", "algae staining", "fungal decay", "insect damage", "root intrusion"],
        "visual_indicators": ["circular lichen colonies", "moss cushions", "green algae staining", "white fungal hyphae", "bore holes"],
        "severity_markers": {
            "mild": "dry exposed surfaces",
            "moderate": "shaded damp surfaces",
            "severe": "perpetually moist, nutrient-rich, sheltered"
        }
    },
    "mechanical": {
        "name": "Mechanical Wear",
        "mechanisms": ["abrasion", "impact", "vibration fatigue", "foot traffic", "wind erosion"],
        "visual_indicators": ["polished wear paths", "chipped edges", "rounded arrises", "smooth concavities", "lost detail"],
        "severity_markers": {
            "mild": "occasional light contact",
            "moderate": "regular handling or foot traffic",
            "severe": "constant abrasion, sand-blast exposure"
        }
    },
    "thermal": {
        "name": "Thermal Cycling",
        "mechanisms": ["expansion-contraction", "differential thermal stress", "fire damage", "frost shattering", "exfoliation"],
        "visual_indicators": ["surface parallel cracks", "exfoliation shells", "fire spalling", "calcination whitening", "curvature from differential expansion"],
        "severity_markers": {
            "mild": "temperate stable climate",
            "moderate": "continental with significant day-night range",
            "severe": "desert extremes, fire exposure, industrial heat"
        }
    }
}

# Conservation condition grades (standard assessment vocabulary)
CONDITION_GRADES = {
    "pristine": {
        "grade": 1,
        "description": "As-made condition, no visible weathering",
        "structural": "fully intact",
        "surface": "original finish unaltered",
        "intervention_needed": "none — preventive conservation only"
    },
    "light_weathering": {
        "grade": 2,
        "description": "Early surface changes, character-enhancing",
        "structural": "fully sound",
        "surface": "minor colour change, initial biological colonization",
        "intervention_needed": "monitoring only"
    },
    "moderate_weathering": {
        "grade": 3,
        "description": "Established patina, stable surface changes",
        "structural": "sound with minor surface loss",
        "surface": "developed patina, established biological growth",
        "intervention_needed": "selective cleaning, biocide if needed"
    },
    "advanced_decay": {
        "grade": 4,
        "description": "Active deterioration requiring intervention",
        "structural": "local weakness, delamination beginning",
        "surface": "significant loss of original surface",
        "intervention_needed": "consolidation, stabilization, repair"
    },
    "severe_deterioration": {
        "grade": 5,
        "description": "Major structural compromise",
        "structural": "critical weakness, risk of collapse/fragmentation",
        "surface": "extensive loss, substrate exposed",
        "intervention_needed": "emergency stabilization, reconstruction"
    },
    "ruin": {
        "grade": 6,
        "description": "Fragmentary remains, archaeological condition",
        "structural": "partial or total loss of structural integrity",
        "surface": "all original surface gone, substrate weathered through",
        "intervention_needed": "documentation, managed decay or reconstruction"
    }
}


# ============================================================================
# Phase 2.6/2.7 Parameter Space Definition
# ============================================================================
#
# Normalized 5D morphospace capturing the full range of weathering aesthetics.
# Each axis maps to a measurable conservation science dimension expressed as
# continuous [0, 1] coordinates for trajectory integration, rhythmic oscillation,
# and attractor analysis.

PATINA_PARAMETER_NAMES = [
    "exposure_duration",     # 0 = freshly made → 1 = ancient/geological time
    "agent_intensity",       # 0 = sheltered/protected → 1 = extreme environmental attack
    "material_resistance",   # 0 = fragile/porous (paper, plaster) → 1 = hard/dense (granite, bronze)
    "intervention_state",    # 0 = untouched natural weathering → 1 = heavily restored/conserved
    "aesthetic_character",   # 0 = ugly/destructive decay → 1 = noble/beautiful patina (wabi-sabi)
]

PATINA_PARAMETER_BOUNDS = [0.0, 1.0]
PATINA_DIMENSIONALITY = 5


# ============================================================================
# 8 Canonical Patina States
# ============================================================================

PATINA_CANONICAL_STATES: Dict[str, Dict[str, float]] = {
    "fresh_pristine": {
        "exposure_duration": 0.00,
        "agent_intensity": 0.00,
        "material_resistance": 0.50,
        "intervention_state": 0.00,
        "aesthetic_character": 0.50,
    },
    "gentle_patina": {
        "exposure_duration": 0.30,
        "agent_intensity": 0.20,
        "material_resistance": 0.60,
        "intervention_state": 0.05,
        "aesthetic_character": 0.85,
    },
    "noble_verdigris": {
        "exposure_duration": 0.60,
        "agent_intensity": 0.45,
        "material_resistance": 0.75,
        "intervention_state": 0.10,
        "aesthetic_character": 0.95,
    },
    "deep_rust": {
        "exposure_duration": 0.55,
        "agent_intensity": 0.70,
        "material_resistance": 0.40,
        "intervention_state": 0.05,
        "aesthetic_character": 0.55,
    },
    "stone_erosion": {
        "exposure_duration": 0.70,
        "agent_intensity": 0.55,
        "material_resistance": 0.65,
        "intervention_state": 0.15,
        "aesthetic_character": 0.75,
    },
    "paper_foxing": {
        "exposure_duration": 0.45,
        "agent_intensity": 0.35,
        "material_resistance": 0.15,
        "intervention_state": 0.20,
        "aesthetic_character": 0.60,
    },
    "cracked_glaze": {
        "exposure_duration": 0.50,
        "agent_intensity": 0.40,
        "material_resistance": 0.55,
        "intervention_state": 0.10,
        "aesthetic_character": 0.80,
    },
    "total_ruin": {
        "exposure_duration": 0.95,
        "agent_intensity": 0.90,
        "material_resistance": 0.30,
        "intervention_state": 0.00,
        "aesthetic_character": 0.40,
    },
}


# ============================================================================
# 6 Visual Types (nearest-neighbor vocabulary targets)
# ============================================================================

PATINA_VISUAL_TYPES = {
    "pristine_surface": {
        "center": {
            "exposure_duration": 0.05, "agent_intensity": 0.05,
            "material_resistance": 0.50, "intervention_state": 0.05,
            "aesthetic_character": 0.50,
        },
        "keywords": [
            "unmarked factory-fresh surface with original tool marks visible",
            "uniform material colour with no environmental alteration",
            "sharp machined edges and crisp geometric arrises",
            "consistent reflectance across all surface orientations",
            "material grain or texture as manufactured without overlay",
        ],
        "optical": {"finish": "original_manufactured", "scatter": "uniform_material", "transparency": "as_made"},
        "color_associations": ["clean whites", "bright metallics", "saturated original pigment", "uniform substrate colour"],
    },
    "warm_aged": {
        "center": {
            "exposure_duration": 0.30, "agent_intensity": 0.20,
            "material_resistance": 0.60, "intervention_state": 0.05,
            "aesthetic_character": 0.85,
        },
        "keywords": [
            "gentle honey-toned warmth from UV-mellowed surface",
            "soft wear at high-contact points revealing substrate warmth",
            "time-enriched surface depth from accumulated micro-interactions",
            "wabi-sabi imperfection enhancing material character and presence",
            "subtle tonal gradation from sheltered-to-exposed transition zones",
        ],
        "optical": {"finish": "mellowed_satin", "scatter": "soft_diffuse", "transparency": "surface_depth"},
        "color_associations": ["honey amber", "warm ivory", "burnished gold", "mellowed cream", "antique white"],
    },
    "oxidation_bloom": {
        "center": {
            "exposure_duration": 0.55, "agent_intensity": 0.55,
            "material_resistance": 0.55, "intervention_state": 0.08,
            "aesthetic_character": 0.75,
        },
        "keywords": [
            "chemical transformation colour visible as surface bloom",
            "verdigris green or rust orange oxide layer over base metal",
            "mottled transition zone where old and new surface coexist",
            "drip-streak staining below oxidation source tracking water path",
            "stable protective patina crust with crystalline micro-texture",
        ],
        "optical": {"finish": "oxide_matte", "scatter": "crystalline_micro", "transparency": "opaque_crust"},
        "color_associations": ["verdigris green", "rust orange-brown", "tarnish purple-black", "oxide red-black", "patina blue-green"],
    },
    "erosion_sculpted": {
        "center": {
            "exposure_duration": 0.70, "agent_intensity": 0.60,
            "material_resistance": 0.60, "intervention_state": 0.12,
            "aesthetic_character": 0.70,
        },
        "keywords": [
            "material subtracted by environmental forces revealing inner structure",
            "rounded edges and dissolved detail softening original geometry",
            "differential erosion where hard and soft zones meet creating relief",
            "honeycomb tafoni cavities carved by salt crystallization cycles",
            "biological colonization establishing in erosion-prepared niches",
        ],
        "optical": {"finish": "rough_textured", "scatter": "deep_shadow_cavity", "transparency": "opaque_solid"},
        "color_associations": ["weathered grey", "lichen orange", "moss green", "exposed substrate pink-buff", "desert varnish brown-black"],
    },
    "fracture_network": {
        "center": {
            "exposure_duration": 0.50, "agent_intensity": 0.45,
            "material_resistance": 0.45, "intervention_state": 0.10,
            "aesthetic_character": 0.75,
        },
        "keywords": [
            "craquelure network dividing surface into irregular polygonal cells",
            "stained crack lines recording moisture penetration history",
            "delamination edge where coating lifts from substrate in curved flakes",
            "conchoidal chip scars exposing fresh substrate colour beneath",
            "alligator-pattern deep cracking from cyclic stress accumulation",
        ],
        "optical": {"finish": "cracked_gloss", "scatter": "linear_shadow_network", "transparency": "layered_partial"},
        "color_associations": ["craze-stained amber", "chip-white substrate", "dark crack-line web", "peeling curl shadow", "glaze pool variation"],
    },
    "archaeological_layer": {
        "center": {
            "exposure_duration": 0.90, "agent_intensity": 0.80,
            "material_resistance": 0.35, "intervention_state": 0.05,
            "aesthetic_character": 0.45,
        },
        "keywords": [
            "multiple temporal states visible simultaneously in cross-section",
            "fragmentary remains with substrate weathered through to core",
            "paint ghosts and stain shadows recording vanished surface layers",
            "advanced biological integration — material becoming landscape",
            "structural collapse geometry revealing internal construction",
        ],
        "optical": {"finish": "friable_rough", "scatter": "deep_multi_layer", "transparency": "fragmentary_void"},
        "color_associations": ["earth tones", "ash grey", "bone white", "charcoal black", "mineral stain ochre"],
    },
}


# ============================================================================
# Visual Vocabulary (parameter-indexed descriptors for prompt generation)
# ============================================================================

PATINA_VISUAL_VOCABULARY = {
    "surface_texture": [
        "pristine smooth surface with original manufactured finish",
        "slight softening of edges from initial environmental contact",
        "developing surface irregularity with micro-texture formation",
        "established rough texture with tactile grain and character",
        "deep surface relief with cavities and raised formations",
        "friable crumbling surface losing structural coherence",
        "granular disaggregation — surface dissolving grain by grain",
        "total surface loss exposing weathered substrate core",
    ],
    "color_transformation": [
        "original material colour unaltered by environment",
        "slight warmth from initial UV mellowing",
        "noticeable colour shift — tarnish warmth or bleaching cool",
        "developed oxide/patina colour overlaying original",
        "dominant new colour from chemical transformation products",
        "mottled patchwork of multiple weathering colour zones",
        "deep complex colour from layered weathering products",
        "fully transformed — no original colour remaining",
    ],
    "structural_integrity": [
        "perfect structural condition — no cracks or deformation",
        "hairline surface cracks not affecting structure",
        "developed crack network with minor delamination beginning",
        "active cracking with measurable displacement at joints",
        "significant delamination — sections lifting from substrate",
        "structural weakness — load-bearing capacity compromised",
        "partial collapse — sections lost with remainder unstable",
        "fragmentary remains — structural system no longer functions",
    ],
    "biological_colonization": [
        "sterile surface — no biological growth present",
        "initial algal greening on damp shaded areas",
        "scattered lichen pioneer colonies establishing",
        "developed lichen communities with multiple species",
        "moss cushions and higher plant colonization in crevices",
        "significant vegetation cover obscuring substrate",
        "dense biological mat — surface largely hidden",
        "full ecological integration — material becoming habitat",
    ],
    "light_interaction": [
        "original reflectance — specular or diffuse as manufactured",
        "slight gloss reduction from surface micro-roughening",
        "matte surface where weathering products scatter light",
        "complex scatter from mixed rough and smooth zones",
        "deep shadow in erosion cavities and crack networks",
        "subsurface glow through translucent patina layers",
        "iridescent interference colours from thin oxide films",
        "light-absorbing friable surface with minimal reflectance",
    ],
    "temporal_evidence": [
        "no visible time markers — could have been made yesterday",
        "subtle signs of age — gentle wear at contact points",
        "clear evidence of years of exposure and use",
        "decades of accumulated environmental interaction visible",
        "multi-generational time depth with repair evidence",
        "century-scale weathering with multiple intervention layers",
        "deep archaeological time — centuries of exposure",
        "geological time markers — millennia of environmental action",
    ],
}


# ============================================================================
# Phase 2.6 Rhythmic Presets
# ============================================================================
#
# Periods chosen to create productive interactions with other domains:
#   16: Unique — fills gap between splash(14) and nuclear/catastrophe(18)
#   18: Shared with nuclear, catastrophe, diatom, splash
#   20: Common period — shared broadly across ecosystem
#   24: Shared near catastrophe/diatom territory
#   30: Major LCM hub — microscopy, diatom, heraldic, surface_design, splash

PATINA_RHYTHMIC_PRESETS = {
    "aging_cycle": {
        "period": 16,
        "state_a": "fresh_pristine",
        "state_b": "deep_rust",
        "pattern": "triangular",
        "description": (
            "Brand-new surface aging into aggressive oxidation and back — "
            "the full lifecycle of ferrous metal under exposure. Unique "
            "period 16 fills gap between splash(14) and shared-18 domains "
            "for novel beat frequencies."
        ),
    },
    "restoration_pendulum": {
        "period": 20,
        "state_a": "total_ruin",
        "state_b": "gentle_patina",
        "pattern": "sinusoidal",
        "description": (
            "Ruin state being gently restored toward dignified age — "
            "the conservation oscillation between decay and intervention. "
            "Syncs with common period 20 across multiple domains."
        ),
    },
    "oxidation_bloom": {
        "period": 24,
        "state_a": "fresh_pristine",
        "state_b": "noble_verdigris",
        "pattern": "sinusoidal",
        "description": (
            "Clean metal surface developing noble green patina — "
            "the copper weathering progression from salmon-pink to blue-green. "
            "Period 24 creates productive interactions near catastrophe/diatom."
        ),
    },
    "erosion_pulse": {
        "period": 18,
        "state_a": "stone_erosion",
        "state_b": "gentle_patina",
        "pattern": "sinusoidal",
        "description": (
            "Stone oscillating between active erosion and gentle stable age — "
            "the tug between environmental attack and material resistance. "
            "Shared period 18 with nuclear/catastrophe/diatom/splash."
        ),
    },
    "entropy_wave": {
        "period": 30,
        "state_a": "gentle_patina",
        "state_b": "total_ruin",
        "pattern": "sinusoidal",
        "description": (
            "Beautiful dignified age descending into complete decay — "
            "the full entropy gradient from wabi-sabi to ruin. "
            "MAJOR LCM HUB period 30 for full-system synchronization."
        ),
    },
}


# ============================================================================
# Phase 2.7 Attractor Presets (Tier 4D Discoveries)
# ============================================================================

PATINA_ATTRACTOR_PRESETS = {
    # ── Tier 1: Stable Cores ──────────────────────────────────────────
    "period_30": {
        "name": "Period 30 — Universal Sync",
        "description": (
            "Dominant LCM synchronization. Patina entropy_wave preset "
            "(period 30) locks directly into this attractor. Surface sits "
            "in the warm-aged territory — gentle time-enriched character "
            "with honey tones and soft wear. The most stable multi-domain "
            "weathering state, analogous to well-maintained antique furniture."
        ),
        "basin_size": 0.116,
        "classification": "lcm_sync",
        "source_domains": ["microscopy", "diatom", "heraldic", "surface_design", "splash", "patina"],
        "state": {
            "exposure_duration": 0.40,
            "agent_intensity": 0.30,
            "material_resistance": 0.55,
            "intervention_state": 0.15,
            "aesthetic_character": 0.75,
        },
    },
    "period_29": {
        "name": "Period 29 — Emergent Resonance",
        "description": (
            "Purely emergent 5-domain attractor. Patina character is a "
            "mid-aged stone surface with established lichen — between "
            "gentle patina and active erosion, with moderate biological "
            "colonization. This weathering state exists nowhere in any "
            "single canonical type."
        ),
        "basin_size": 0.084,
        "classification": "lcm_sync",
        "source_domains": ["microscopy", "nuclear", "catastrophe", "diatom", "heraldic"],
        "state": {
            "exposure_duration": 0.55,
            "agent_intensity": 0.40,
            "material_resistance": 0.60,
            "intervention_state": 0.10,
            "aesthetic_character": 0.70,
        },
    },
    "period_19": {
        "name": "Period 19 — Gap Flow",
        "description": (
            "Resilient novel gap-filler between periods 18 and 20. "
            "Patina is a precise oxidation-bloom state — the exact "
            "moment copper turns from brown cuprite to green verdigris, "
            "poised at the chemical transition boundary. "
            "Prime-period irrational beats."
        ),
        "basin_size": 0.074,
        "classification": "novel",
        "source_domains": ["microscopy", "nuclear", "catastrophe", "diatom"],
        "state": {
            "exposure_duration": 0.48,
            "agent_intensity": 0.42,
            "material_resistance": 0.65,
            "intervention_state": 0.08,
            "aesthetic_character": 0.82,
        },
    },
    # ── Tier 2: Specialized ───────────────────────────────────────────
    "period_28": {
        "name": "Period 28 — Composite Beat",
        "description": (
            "Novel composite beat. Patina sits in tension between "
            "noble beauty and advancing decay — the cracked-glaze "
            "state where craquelure network is simultaneously beautiful "
            "pattern and active deterioration pathway. The conservation "
            "equivalent of a held breath."
        ),
        "basin_size": 0.024,
        "classification": "novel",
        "source_domains": ["microscopy", "nuclear", "catastrophe", "diatom"],
        "state": {
            "exposure_duration": 0.52,
            "agent_intensity": 0.48,
            "material_resistance": 0.50,
            "intervention_state": 0.12,
            "aesthetic_character": 0.72,
        },
    },
    "period_60": {
        "name": "Period 60 — Harmonic Hub",
        "description": (
            "Major LCM hub (3×20, 4×15, 5×12). Patina oscillates through "
            "full weathering repertoire — every canonical state gets a "
            "moment in the long cycle. Complex synchronization, advanced use."
        ),
        "basin_size": 0.040,
        "classification": "harmonic",
        "source_domains": ["microscopy", "nuclear", "catastrophe", "diatom"],
        "state": {
            "exposure_duration": 0.50,
            "agent_intensity": 0.45,
            "material_resistance": 0.52,
            "intervention_state": 0.10,
            "aesthetic_character": 0.65,
        },
    },
    # ── Tier 3: Curated Edge States ───────────────────────────────────
    "bifurcation_edge": {
        "name": "Bifurcation Edge — Patina Threshold",
        "description": (
            "Curated state at the exact moment weathering transitions from "
            "character-enhancing patina to destructive decay. Poised between "
            "warm_aged and erosion_sculpted basins — the conservation "
            "threshold where 'beautiful age' becomes 'active deterioration'. "
            "The most consequential moment in any material's lifecycle."
        ),
        "basin_size": None,
        "classification": "curated",
        "source_domains": ["patina"],
        "state": {
            "exposure_duration": 0.52,
            "agent_intensity": 0.50,
            "material_resistance": 0.48,
            "intervention_state": 0.05,
            "aesthetic_character": 0.65,
        },
    },
    "organic_complexity": {
        "name": "Organic Complexity — Wabi-Sabi Perfection",
        "description": (
            "Curated state at maximum aesthetic beauty from weathering. "
            "The wabi-sabi ideal — time has enriched rather than degraded. "
            "Worn smooth by hands, mellowed by light, dignified by years. "
            "Not ancient ruin but perfected age."
        ),
        "basin_size": None,
        "classification": "curated",
        "source_domains": ["patina"],
        "state": {
            "exposure_duration": 0.35,
            "agent_intensity": 0.20,
            "material_resistance": 0.70,
            "intervention_state": 0.10,
            "aesthetic_character": 0.95,
        },
    },
}


# ============================================================================
# Phase 2.6/2.7 Helper Functions
# ============================================================================

def _patina_euclidean_distance(a: Dict[str, float], b: Dict[str, float]) -> float:
    """Euclidean distance between two states in patina parameter space."""
    return math.sqrt(sum((a[p] - b[p]) ** 2 for p in PATINA_PARAMETER_NAMES))


def _patina_nearest_canonical(state: Dict[str, float]) -> tuple:
    """Find nearest canonical patina state. Returns (state_id, distance)."""
    best_id, best_dist = None, float("inf")
    for sid, coords in PATINA_CANONICAL_STATES.items():
        d = _patina_euclidean_distance(state, coords)
        if d < best_dist:
            best_id, best_dist = sid, d
    return best_id, best_dist


def _patina_nearest_visual_type(state: Dict[str, float]) -> tuple:
    """Find nearest patina visual type. Returns (type_id, distance)."""
    best_id, best_dist = None, float("inf")
    for vid, vdata in PATINA_VISUAL_TYPES.items():
        d = _patina_euclidean_distance(state, vdata["center"])
        if d < best_dist:
            best_id, best_dist = vid, d
    return best_id, best_dist


def _patina_interpolate_states(
    state_a: Dict[str, float],
    state_b: Dict[str, float],
    t: float,
    pattern: str = "sinusoidal",
) -> Dict[str, float]:
    """Interpolate between two patina states at phase t ∈ [0, 1]."""
    if pattern == "sinusoidal":
        alpha = 0.5 * (1.0 - math.cos(math.pi * t))
    elif pattern == "triangular":
        alpha = 2.0 * t if t <= 0.5 else 2.0 * (1.0 - t)
    elif pattern == "square":
        alpha = 0.0 if t < 0.5 else 1.0
    else:
        alpha = t
    return {
        p: state_a[p] + alpha * (state_b[p] - state_a[p])
        for p in PATINA_PARAMETER_NAMES
    }


def _patina_select_vocabulary(state: Dict[str, float]) -> Dict[str, List[str]]:
    """Select vocabulary terms weighted by patina parameter values."""
    selected = {}
    for category, terms in PATINA_VISUAL_VOCABULARY.items():
        if category == "surface_texture":
            idx = round(state["exposure_duration"] * (len(terms) - 1))
        elif category == "color_transformation":
            # Combine exposure and agent intensity
            v = (state["exposure_duration"] + state["agent_intensity"]) / 2.0
            idx = round(v * (len(terms) - 1))
        elif category == "structural_integrity":
            # High agent + low resistance = more damage
            v = state["agent_intensity"] * (1.0 - state["material_resistance"] * 0.5)
            idx = round(v * (len(terms) - 1))
        elif category == "biological_colonization":
            # Combine exposure time and agent intensity (biological component)
            v = (state["exposure_duration"] * 0.6 + state["agent_intensity"] * 0.4)
            idx = round(v * (len(terms) - 1))
        elif category == "light_interaction":
            # Complex: age and intervention both affect this
            v = state["exposure_duration"] * 0.5 + state["agent_intensity"] * 0.3 + (1.0 - state["intervention_state"]) * 0.2
            idx = round(v * (len(terms) - 1))
        elif category == "temporal_evidence":
            idx = round(state["exposure_duration"] * (len(terms) - 1))
        else:
            idx = 0

        idx = max(0, min(idx, len(terms) - 1))
        neighbors = [
            terms[max(0, idx - 1)],
            terms[idx],
            terms[min(len(terms) - 1, idx + 1)],
        ]
        selected[category] = list(dict.fromkeys(neighbors))  # deduplicate
    return selected


def _extract_keywords(text: str) -> Dict[str, List[str]]:
    """Extract relevant keywords from text for intent classification."""
    text_lower = text.lower()
    matches = {"materials": [], "agents": [], "conditions": [], "aesthetics": []}

    # Material keywords
    material_patterns = {
        "ferrous_metal": ["iron", "steel", "rust", "rusted", "rusting", "corten", "ferrous"],
        "copper_alloy": ["copper", "bronze", "brass", "verdigris", "patina green"],
        "silver": ["silver", "tarnish", "tarnished", "sterling"],
        "limestone": ["limestone", "marble", "chalk", "calcite"],
        "sandstone": ["sandstone", "brownstone", "sandblast"],
        "wood": ["wood", "timber", "oak", "cedar", "driftwood", "wooden"],
        "ceramic_glaze": ["ceramic", "porcelain", "pottery", "glaze", "terracotta", "craquelure"],
        "paper_textile": ["paper", "canvas", "textile", "fabric", "vellum", "parchment", "linen"],
        "paint_coating": ["paint", "painted", "lacquer", "varnish", "coating", "peeling paint"],
        "concrete": ["concrete", "cement", "brutalist", "rebar"],
        "glass": ["glass", "stained glass", "iridescent glass"],
    }
    for mat, patterns in material_patterns.items():
        for p in patterns:
            if p in text_lower:
                matches["materials"].append(mat)
                break

    # Agent keywords
    agent_patterns = {
        "water": ["rain", "water", "flood", "moisture", "wet", "damp", "coastal", "salt spray"],
        "uv_solar": ["sun", "uv", "faded", "fading", "bleach", "solar"],
        "chemical": ["acid", "pollution", "sulfur", "corrosion", "industrial"],
        "biological": ["lichen", "moss", "algae", "fungal", "mold", "ivy", "overgrown"],
        "mechanical": ["worn", "abraded", "polished", "traffic", "scratched", "chipped"],
        "thermal": ["fire", "burned", "frost", "frozen", "heat", "calcined"],
    }
    for agent, patterns in agent_patterns.items():
        for p in patterns:
            if p in text_lower:
                matches["agents"].append(agent)
                break

    # Condition keywords
    condition_patterns = {
        "pristine": ["new", "pristine", "fresh", "mint", "unused", "unworn"],
        "light_weathering": ["slightly aged", "gentle wear", "mild patina", "light weathering"],
        "moderate_weathering": ["aged", "weathered", "patinated", "worn", "used", "vintage"],
        "advanced_decay": ["decayed", "deteriorated", "damaged", "crumbling"],
        "severe_deterioration": ["ruined", "derelict", "abandoned", "collapsed"],
        "ruin": ["ruin", "ruins", "archaeological", "ancient", "fragment"],
    }
    for cond, patterns in condition_patterns.items():
        for p in patterns:
            if p in text_lower:
                matches["conditions"].append(cond)
                break

    # Aesthetic keywords
    aesthetic_patterns = {
        "wabi_sabi": ["wabi", "sabi", "wabi-sabi", "imperfect beauty", "noble age"],
        "industrial": ["industrial", "brutalist", "raw", "gritty"],
        "romantic_ruin": ["romantic ruin", "picturesque", "overgrown", "reclaimed by nature"],
        "conservation": ["conserved", "restored", "stabilized", "repaired"],
        "kintsugi": ["kintsugi", "gold repair", "visible mend", "embracing damage"],
    }
    for aes, patterns in aesthetic_patterns.items():
        for p in patterns:
            if p in text_lower:
                matches["aesthetics"].append(aes)
                break

    return matches


# ============================================================================
# LAYER 1: Pure Taxonomy Tools (0 tokens)
# ============================================================================

@mcp.tool()
def list_material_categories() -> str:
    """
    List all material categories with characteristic weathering behaviors.

    LAYER 1: Pure taxonomy enumeration (0 LLM tokens).

    Returns overview of 11 material categories:
    - Ferrous metals (iron, steel → rust)
    - Copper alloys (bronze, brass → verdigris)
    - Silver (sterling → tarnish)
    - Limestone & Marble (dissolution, sugaring)
    - Sandstone (granular disaggregation, tafoni)
    - Wood (silvering, checking, biological colonization)
    - Ceramics & Glazes (craquelure, spalling)
    - Paper & Textiles (foxing, yellowing)
    - Paint & Coatings (peeling, alligatoring)
    - Concrete (spalling, efflorescence)
    - Glass (devitrification, iridescence)

    Returns:
        JSON with all material category specifications
    """
    result = {}
    for mat_id, mat_data in MATERIAL_CATEGORIES.items():
        result[mat_id] = {
            "name": mat_data["name"],
            "description": mat_data["description"],
            "primary_weathering": mat_data["primary_weathering"],
            "characteristic_patina": mat_data["characteristic_patina"],
            "examples": mat_data["examples"],
        }
    return json.dumps({
        "material_categories": result,
        "total_categories": len(result),
    }, indent=2)


@mcp.tool()
def get_material_details(material_id: str) -> str:
    """
    Get complete specification for a material category.

    LAYER 1: Pure taxonomy retrieval (0 LLM tokens).

    Args:
        material_id: One of: ferrous_metal, copper_alloy, silver, limestone,
                     sandstone, wood, ceramic_glaze, paper_textile,
                     paint_coating, concrete, glass

    Returns:
        JSON with complete weathering progression and visual markers
    """
    if material_id not in MATERIAL_CATEGORIES:
        return json.dumps({
            "error": f"Unknown material: {material_id}",
            "available": list(MATERIAL_CATEGORIES.keys()),
        })
    return json.dumps(MATERIAL_CATEGORIES[material_id], indent=2)


@mcp.tool()
def list_weathering_agents() -> str:
    """
    List all weathering agent categories with mechanisms and visual indicators.

    LAYER 1: Pure taxonomy enumeration (0 LLM tokens).

    Returns overview of 6 agent categories:
    - Water (dissolution, freeze-thaw, salt crystallization)
    - UV/Solar (fading, chalking, embrittlement)
    - Chemical (acid rain, sulfation, galvanic corrosion)
    - Biological (lichen, moss, fungal decay, insect damage)
    - Mechanical (abrasion, impact, foot traffic)
    - Thermal (expansion-contraction, fire damage, frost shattering)
    """
    result = {}
    for agent_id, agent_data in WEATHERING_AGENTS.items():
        result[agent_id] = {
            "name": agent_data["name"],
            "mechanisms": agent_data["mechanisms"],
            "visual_indicators": agent_data["visual_indicators"],
        }
    return json.dumps({
        "weathering_agents": result,
        "total_agents": len(result),
    }, indent=2)


@mcp.tool()
def get_weathering_agent_details(agent_id: str) -> str:
    """
    Get complete specification for a weathering agent.

    LAYER 1: Pure taxonomy retrieval (0 LLM tokens).

    Args:
        agent_id: One of: water, uv_solar, chemical, biological,
                  mechanical, thermal
    """
    if agent_id not in WEATHERING_AGENTS:
        return json.dumps({
            "error": f"Unknown agent: {agent_id}",
            "available": list(WEATHERING_AGENTS.keys()),
        })
    return json.dumps(WEATHERING_AGENTS[agent_id], indent=2)


@mcp.tool()
def list_condition_grades() -> str:
    """
    List conservation condition grades from pristine to ruin.

    LAYER 1: Pure taxonomy enumeration (0 LLM tokens).

    Standard 6-grade assessment scale used in conservation science:
    1. Pristine — as-made
    2. Light weathering — character-enhancing
    3. Moderate weathering — stable patina
    4. Advanced decay — active deterioration
    5. Severe deterioration — structural compromise
    6. Ruin — fragmentary remains
    """
    return json.dumps({
        "condition_grades": CONDITION_GRADES,
        "total_grades": len(CONDITION_GRADES),
    }, indent=2)


# ============================================================================
# LAYER 2: Deterministic Mapping Tools (0 tokens)
# ============================================================================

@mcp.tool()
def classify_weathering_intent(user_intent: str) -> str:
    """
    Classify weathering intent from user description.

    LAYER 2: Deterministic keyword matching (0 LLM tokens).

    Analyzes intent text and matches against material, agent, condition,
    and aesthetic keyword patterns.

    Args:
        user_intent: User's description of desired weathering aesthetic

    Returns:
        JSON with classification: material, agents, condition grade,
        aesthetic mode, and matched keywords.
    """
    matches = _extract_keywords(user_intent)

    # Determine primary material
    primary_material = matches["materials"][0] if matches["materials"] else "ferrous_metal"

    # Determine primary agents
    primary_agents = matches["agents"] if matches["agents"] else ["water", "uv_solar"]

    # Determine condition grade
    if matches["conditions"]:
        condition = matches["conditions"][0]
    else:
        # Infer from other clues
        intent_lower = user_intent.lower()
        if any(w in intent_lower for w in ["old", "ancient", "centuries"]):
            condition = "advanced_decay"
        elif any(w in intent_lower for w in ["aged", "vintage", "antique"]):
            condition = "moderate_weathering"
        elif any(w in intent_lower for w in ["new", "clean", "fresh"]):
            condition = "pristine"
        else:
            condition = "moderate_weathering"

    # Determine aesthetic mode
    aesthetic = matches["aesthetics"][0] if matches["aesthetics"] else "wabi_sabi"

    # Map condition to nearest canonical state
    condition_to_canonical = {
        "pristine": "fresh_pristine",
        "light_weathering": "gentle_patina",
        "moderate_weathering": "noble_verdigris",
        "advanced_decay": "deep_rust",
        "severe_deterioration": "stone_erosion",
        "ruin": "total_ruin",
    }
    canonical_state = condition_to_canonical.get(condition, "gentle_patina")

    # Confidence based on keyword matches
    total_matches = sum(len(v) for v in matches.values())
    confidence = min(total_matches / 5.0, 1.0)

    return json.dumps({
        "primary_material": primary_material,
        "material_details": {
            "name": MATERIAL_CATEGORIES[primary_material]["name"],
            "characteristic_patina": MATERIAL_CATEGORIES[primary_material]["characteristic_patina"],
        },
        "primary_agents": primary_agents,
        "condition_grade": condition,
        "condition_details": CONDITION_GRADES[condition],
        "aesthetic_mode": aesthetic,
        "nearest_canonical_state": canonical_state,
        "confidence": round(max(confidence, 0.3), 2),
        "matched_keywords": matches,
    }, indent=2)


@mcp.tool()
def map_weathering_parameters(
    material_id: str,
    condition_grade: str = "moderate_weathering",
    primary_agent: str = "water",
    intensity: str = "moderate",
    emphasis: str = "surface",
) -> str:
    """
    Map weathering specification to visual parameters for image generation.

    Layer 2: Deterministic operation (0 tokens).

    Args:
        material_id: Material category ID
        condition_grade: Conservation condition grade
        primary_agent: Dominant weathering agent
        intensity: subtle, moderate, or dramatic
        emphasis: surface, color, structure, biological, or temporal

    Returns:
        Complete parameter set for visual synthesis including vocabulary
        weighted by intensity and emphasis.
    """
    if material_id not in MATERIAL_CATEGORIES:
        return json.dumps({"error": f"Unknown material: {material_id}", "available": list(MATERIAL_CATEGORIES.keys())})
    if condition_grade not in CONDITION_GRADES:
        return json.dumps({"error": f"Unknown grade: {condition_grade}", "available": list(CONDITION_GRADES.keys())})

    mat = MATERIAL_CATEGORIES[material_id]
    grade = CONDITION_GRADES[condition_grade]
    agent = WEATHERING_AGENTS.get(primary_agent, WEATHERING_AGENTS["water"])

    # Map condition grade to approximate canonical state
    grade_to_state = {
        "pristine": "fresh_pristine",
        "light_weathering": "gentle_patina",
        "moderate_weathering": "noble_verdigris" if material_id in ["copper_alloy"] else "cracked_glaze",
        "advanced_decay": "deep_rust" if material_id in ["ferrous_metal"] else "stone_erosion",
        "severe_deterioration": "stone_erosion",
        "ruin": "total_ruin",
    }
    state_id = grade_to_state.get(condition_grade, "gentle_patina")
    state = PATINA_CANONICAL_STATES[state_id]

    vtype, vdist = _patina_nearest_visual_type(state)
    vdata = PATINA_VISUAL_TYPES[vtype]
    vocab = _patina_select_vocabulary(state)

    intensity_weights = {"subtle": 0.6, "moderate": 1.0, "dramatic": 1.5}
    weight = intensity_weights.get(intensity, 1.0)

    # Select emphasis category
    emphasis_map = {
        "surface": "surface_texture",
        "color": "color_transformation",
        "structure": "structural_integrity",
        "biological": "biological_colonization",
        "temporal": "temporal_evidence",
        "light": "light_interaction",
    }
    primary_cat = emphasis_map.get(emphasis, "surface_texture")
    primary_terms = vocab.get(primary_cat, [])

    # Select material-specific visual markers for the condition grade
    grade_index = grade["grade"] - 1
    marker_index = min(grade_index, len(mat["visual_markers"]) - 1)
    material_markers = mat["visual_markers"][max(0, marker_index - 1):marker_index + 2]

    # Color from progression
    color_index = min(grade_index, len(mat["color_progression"]) - 1)
    current_color = mat["color_progression"][color_index]

    return json.dumps({
        "material_id": material_id,
        "material_name": mat["name"],
        "condition_grade": condition_grade,
        "primary_agent": primary_agent,
        "intensity": intensity,
        "emphasis": emphasis,
        "weight": weight,
        "state": state,
        "nearest_visual_type": vtype,
        "visual_distance": round(vdist, 4),
        "optical_properties": vdata["optical"],
        "current_color_stage": current_color,
        "material_specific_markers": material_markers,
        "agent_visual_indicators": agent["visual_indicators"],
        "primary_vocabulary": primary_terms,
        "full_vocabulary": vocab,
        "keywords": vdata["keywords"],
        "color_associations": vdata["color_associations"],
    }, indent=2)


# ============================================================================
# LAYER 3: Claude Synthesis Interface
# ============================================================================

@mcp.tool()
def enhance_patina_prompt(
    user_intent: str,
    material_override: Optional[str] = None,
    condition_override: Optional[str] = None,
    intensity: str = "moderate",
) -> str:
    """
    Prepare complete patina/weathering enhancement for Claude synthesis.

    LAYER 3 INTERFACE: Combines Layer 1 & 2 outputs into structured
    data ready for Claude to synthesize into an enhanced image prompt.

    This tool does NOT synthesize the final prompt — it provides all
    deterministic parameters for Claude to creatively compose.

    Args:
        user_intent: User's description of desired weathering aesthetic
        material_override: Optional specific material (auto-detected if not provided)
        condition_override: Optional condition grade
        intensity: Enhancement intensity (subtle, moderate, dramatic)

    Returns:
        JSON with complete enhancement package for Claude synthesis
    """
    # Classify intent
    classification = json.loads(classify_weathering_intent(user_intent))

    material_id = material_override or classification["primary_material"]
    condition = condition_override or classification["condition_grade"]
    primary_agent = classification["primary_agents"][0] if classification["primary_agents"] else "water"

    # Get full parameter mapping
    params = json.loads(map_weathering_parameters(
        material_id=material_id,
        condition_grade=condition,
        primary_agent=primary_agent,
        intensity=intensity,
    ))

    mat = MATERIAL_CATEGORIES[material_id]

    return json.dumps({
        "original_intent": user_intent,
        "intensity": intensity,
        "classification": classification,
        "weathering_specification": params,
        "material_context": {
            "name": mat["name"],
            "characteristic_patina": mat["characteristic_patina"],
            "color_progression": mat["color_progression"],
            "time_scale": mat["time_scale"],
        },
        "synthesis_instructions": {
            "task": "Synthesize image generation prompt from deterministic weathering parameters",
            "approach": "Translate conservation science taxonomy into concrete visual descriptors",
            "emphasis": f"Apply {intensity} intensity to vocabulary selection",
            "guidelines": [
                "Use material_specific_markers for physical accuracy",
                "Reference color_progression for current weathering stage",
                "Translate agent_visual_indicators into observable surface evidence",
                "Maintain specificity — name the oxide, the organism, the fracture mode",
                "Preserve the aesthetic_character value (wabi-sabi vs destructive)",
                "Describe patina as surface evidence not metaphor",
            ],
        },
    }, indent=2)


# ============================================================================
# PHASE 2.6: Rhythmic Composition Tools (0 tokens)
# ============================================================================

@mcp.tool()
def get_patina_canonical_states() -> str:
    """
    List all 8 canonical patina states with their 5D parameter coordinates.

    Layer 1: Pure taxonomy lookup (0 tokens).
    """
    result = {}
    for sid, coords in PATINA_CANONICAL_STATES.items():
        vtype, vdist = _patina_nearest_visual_type(coords)
        result[sid] = {
            "coordinates": coords,
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
        }
    return json.dumps({
        "canonical_states": result,
        "parameter_names": PATINA_PARAMETER_NAMES,
        "dimensionality": PATINA_DIMENSIONALITY,
        "total_states": len(result),
    }, indent=2)


@mcp.tool()
def get_patina_visual_types() -> str:
    """
    List all 6 patina visual types with keywords and optical properties.

    Layer 1: Pure taxonomy lookup (0 tokens).

    Visual types are nearest-neighbor targets used for vocabulary extraction.
    Each type has center coordinates, 5 image-generation keywords, and
    optical finish/scatter/transparency properties.
    """
    result = {}
    for vid, vdata in PATINA_VISUAL_TYPES.items():
        result[vid] = {
            "center": vdata["center"],
            "keywords": vdata["keywords"],
            "optical": vdata["optical"],
            "color_associations": vdata["color_associations"],
        }
    return json.dumps({
        "visual_types": result,
        "total_types": len(result),
        "parameter_names": PATINA_PARAMETER_NAMES,
    }, indent=2)


@mcp.tool()
def list_patina_rhythmic_presets() -> str:
    """
    List all 5 Phase 2.6 rhythmic presets for patina aesthetics.

    Layer 2: Pure lookup (0 tokens).

    Presets oscillate between two canonical patina states, creating
    temporal aesthetic composition suitable for animation keyframes,
    storyboard sequences, and multi-domain compositional limit cycles.

    Available presets:
        aging_cycle (16):            pristine ↔ deep_rust
        restoration_pendulum (20):   total_ruin ↔ gentle_patina
        oxidation_bloom (24):        pristine ↔ noble_verdigris
        erosion_pulse (18):          stone_erosion ↔ gentle_patina
        entropy_wave (30):           gentle_patina ↔ total_ruin
    """
    result = {}
    for name, cfg in PATINA_RHYTHMIC_PRESETS.items():
        result[name] = {
            "period": cfg["period"],
            "state_a": cfg["state_a"],
            "state_b": cfg["state_b"],
            "pattern": cfg["pattern"],
            "description": cfg["description"],
        }
    return json.dumps({
        "presets": result,
        "total_presets": len(result),
        "periods": sorted(set(c["period"] for c in PATINA_RHYTHMIC_PRESETS.values())),
    }, indent=2)


@mcp.tool()
def apply_patina_rhythmic_preset(preset_name: str) -> str:
    """
    Apply a curated patina rhythmic pattern preset.

    Layer 2: Deterministic sequence generation (0 tokens).

    Generates a complete oscillation sequence showing how the weathering
    aesthetic evolves over one full period.

    Args:
        preset_name: One of aging_cycle, restoration_pendulum, oxidation_bloom,
                     erosion_pulse, entropy_wave
    """
    if preset_name not in PATINA_RHYTHMIC_PRESETS:
        return json.dumps({
            "error": f"Unknown preset: {preset_name}",
            "available": list(PATINA_RHYTHMIC_PRESETS.keys()),
        })

    cfg = PATINA_RHYTHMIC_PRESETS[preset_name]
    state_a = PATINA_CANONICAL_STATES[cfg["state_a"]]
    state_b = PATINA_CANONICAL_STATES[cfg["state_b"]]
    period = cfg["period"]

    sequence = []
    for step in range(period):
        t = step / period
        state = _patina_interpolate_states(state_a, state_b, t, cfg["pattern"])
        vtype, vdist = _patina_nearest_visual_type(state)
        sequence.append({
            "step": step,
            "phase": round(t, 4),
            "state": {k: round(v, 4) for k, v in state.items()},
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
        })

    return json.dumps({
        "preset": preset_name,
        "period": period,
        "pattern": cfg["pattern"],
        "state_a": cfg["state_a"],
        "state_b": cfg["state_b"],
        "description": cfg["description"],
        "sequence": sequence,
        "total_steps": len(sequence),
    }, indent=2)


@mcp.tool()
def generate_patina_rhythmic_sequence(
    state_a_id: str,
    state_b_id: str,
    oscillation_pattern: str = "sinusoidal",
    num_cycles: int = 3,
    steps_per_cycle: int = 20,
    phase_offset: float = 0.0,
) -> str:
    """
    Generate custom rhythmic oscillation between any two patina states.

    Layer 2: Temporal composition (0 tokens).

    Args:
        state_a_id: Starting patina state (one of 8 canonical IDs)
        state_b_id: Alternating patina state
        oscillation_pattern: sinusoidal, triangular, or square
        num_cycles: Number of complete A→B→A cycles
        steps_per_cycle: Samples per cycle
        phase_offset: Starting phase (0.0 = A, 0.5 = B)
    """
    if state_a_id not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {state_a_id}", "available": list(PATINA_CANONICAL_STATES.keys())})
    if state_b_id not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {state_b_id}", "available": list(PATINA_CANONICAL_STATES.keys())})

    state_a = PATINA_CANONICAL_STATES[state_a_id]
    state_b = PATINA_CANONICAL_STATES[state_b_id]
    total_steps = num_cycles * steps_per_cycle

    sequence = []
    for step in range(total_steps):
        raw_t = step / steps_per_cycle + phase_offset
        t = raw_t % 1.0
        state = _patina_interpolate_states(state_a, state_b, t, oscillation_pattern)
        vtype, vdist = _patina_nearest_visual_type(state)
        sequence.append({
            "step": step,
            "cycle": step // steps_per_cycle,
            "phase": round(t, 4),
            "state": {k: round(v, 4) for k, v in state.items()},
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
        })

    return json.dumps({
        "state_a": state_a_id,
        "state_b": state_b_id,
        "pattern": oscillation_pattern,
        "num_cycles": num_cycles,
        "steps_per_cycle": steps_per_cycle,
        "phase_offset": phase_offset,
        "total_steps": total_steps,
        "sequence": sequence,
    }, indent=2)


@mcp.tool()
def compute_patina_distance(patina_id_1: str, patina_id_2: str) -> str:
    """
    Compute distance between two patina states in 5D parameter space.

    Layer 2: Pure distance computation (0 tokens).

    Args:
        patina_id_1: First canonical patina state
        patina_id_2: Second canonical patina state
    """
    if patina_id_1 not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {patina_id_1}", "available": list(PATINA_CANONICAL_STATES.keys())})
    if patina_id_2 not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {patina_id_2}", "available": list(PATINA_CANONICAL_STATES.keys())})

    a = PATINA_CANONICAL_STATES[patina_id_1]
    b = PATINA_CANONICAL_STATES[patina_id_2]
    diffs = {p: round(b[p] - a[p], 4) for p in PATINA_PARAMETER_NAMES}
    dist = _patina_euclidean_distance(a, b)

    return json.dumps({
        "patina_id_1": patina_id_1,
        "patina_id_2": patina_id_2,
        "euclidean_distance": round(dist, 4),
        "per_parameter_diff": diffs,
        "abs_per_parameter": {p: round(abs(v), 4) for p, v in diffs.items()},
        "max_parameter_diff": round(max(abs(v) for v in diffs.values()), 4),
        "dominant_axis": max(diffs, key=lambda p: abs(diffs[p])),
    }, indent=2)


@mcp.tool()
def compute_patina_trajectory(
    start_patina_id: str,
    end_patina_id: str,
    num_steps: int = 20,
) -> str:
    """
    Compute smooth trajectory between two patina states in morphospace.

    Layer 2: Deterministic trajectory integration (0 tokens).

    Enables visualization of smooth weathering transitions — e.g.,
    fresh_pristine gradually becoming noble_verdigris.

    Args:
        start_patina_id: Starting canonical patina state
        end_patina_id: Target canonical patina state
        num_steps: Number of interpolation steps (default: 20)
    """
    if start_patina_id not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {start_patina_id}", "available": list(PATINA_CANONICAL_STATES.keys())})
    if end_patina_id not in PATINA_CANONICAL_STATES:
        return json.dumps({"error": f"Unknown: {end_patina_id}", "available": list(PATINA_CANONICAL_STATES.keys())})

    a = PATINA_CANONICAL_STATES[start_patina_id]
    b = PATINA_CANONICAL_STATES[end_patina_id]
    total_dist = _patina_euclidean_distance(a, b)

    trajectory = []
    for i in range(num_steps + 1):
        t = i / num_steps
        state = {p: round(a[p] + t * (b[p] - a[p]), 4) for p in PATINA_PARAMETER_NAMES}
        vtype, vdist = _patina_nearest_visual_type(state)
        nearest_canon, cdist = _patina_nearest_canonical(state)
        trajectory.append({
            "step": i,
            "t": round(t, 4),
            "state": state,
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
            "nearest_canonical": nearest_canon,
            "canonical_distance": round(cdist, 4),
        })

    return json.dumps({
        "start": start_patina_id,
        "end": end_patina_id,
        "total_distance": round(total_dist, 4),
        "num_steps": num_steps,
        "trajectory": trajectory,
    }, indent=2)


@mcp.tool()
def extract_patina_visual_vocabulary(
    state: Optional[Dict[str, float]] = None,
    patina_id: Optional[str] = None,
    strength: float = 1.0,
) -> str:
    """
    Extract visual vocabulary from patina parameter coordinates.

    Layer 2: Deterministic vocabulary mapping (0 tokens).

    Maps a 5D parameter state to the nearest visual type and returns
    image-generation-ready keywords with optical properties.

    Args:
        state: Parameter coordinates dict. Provide either state or patina_id.
        patina_id: Canonical patina state to use as state source.
        strength: Keyword weight multiplier [0.0, 1.0] (default: 1.0)
    """
    if state is None and patina_id is None:
        return json.dumps({"error": "Provide either state or patina_id"})
    if patina_id is not None:
        if patina_id not in PATINA_CANONICAL_STATES:
            return json.dumps({"error": f"Unknown: {patina_id}", "available": list(PATINA_CANONICAL_STATES.keys())})
        state = PATINA_CANONICAL_STATES[patina_id]

    for p in PATINA_PARAMETER_NAMES:
        if p not in state:
            return json.dumps({"error": f"Missing parameter: {p}", "required": PATINA_PARAMETER_NAMES})

    vtype, vdist = _patina_nearest_visual_type(state)
    vdata = PATINA_VISUAL_TYPES[vtype]
    vocab = _patina_select_vocabulary(state)
    nearest_canon, cdist = _patina_nearest_canonical(state)

    return json.dumps({
        "nearest_visual_type": vtype,
        "distance": round(vdist, 4),
        "keywords": vdata["keywords"],
        "optical_properties": vdata["optical"],
        "color_associations": vdata["color_associations"],
        "nearest_canonical_state": nearest_canon,
        "canonical_distance": round(cdist, 4),
        "vocabulary_by_category": vocab,
        "strength": strength,
        "input_state": {k: round(v, 4) for k, v in state.items()},
    }, indent=2)


# ============================================================================
# PHASE 2.7: Attractor Visualization Prompt Generation (0 tokens)
# ============================================================================

@mcp.tool()
def list_patina_attractor_presets() -> str:
    """
    List all 7 discovered/curated attractor presets for patina visualization.

    Layer 2: Pure lookup (0 tokens).

    Attractor presets represent multi-domain emergent states mapped to
    patina parameter coordinates. Each encodes the weathering aesthetic
    that arises when the system locks into that attractor period during
    multi-domain composition.
    """
    result = {}
    for aid, adata in PATINA_ATTRACTOR_PRESETS.items():
        vtype, vdist = _patina_nearest_visual_type(adata["state"])
        result[aid] = {
            "name": adata["name"],
            "description": adata["description"],
            "basin_size": adata["basin_size"],
            "classification": adata["classification"],
            "source_domains": adata["source_domains"],
            "state": adata["state"],
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
        }
    return json.dumps({
        "attractor_presets": result,
        "total_presets": len(result),
        "parameter_names": PATINA_PARAMETER_NAMES,
    }, indent=2)


@mcp.tool()
def generate_patina_attractor_prompt(
    attractor_id: str = "",
    custom_state: Optional[Dict[str, float]] = None,
    mode: str = "composite",
    style_modifier: str = "",
    keyframe_count: int = 4,
) -> str:
    """
    Generate image generation prompt from attractor state or custom coordinates.

    Layer 2: Deterministic prompt synthesis (0 tokens).

    Translates patina aesthetic coordinates into visual prompts suitable
    for ComfyUI, Stable Diffusion, DALL-E, etc.

    Modes:
        composite:  Single blended prompt from attractor state
        split_view: Separate prompt per vocabulary category
        sequence:   Multiple keyframe prompts from nearest rhythmic preset

    Args:
        attractor_id: Preset attractor name (period_30, period_19, etc.)
        custom_state: Optional custom parameter coordinates dict.
        mode: composite | split_view | sequence
        style_modifier: Optional prefix (e.g. "close-up photograph", "oil painting")
        keyframe_count: Number of keyframes for sequence mode (default: 4)
    """
    # ── Resolve state ─────────────────────────────────────────────────
    attractor_meta = None
    if custom_state is not None:
        for p in PATINA_PARAMETER_NAMES:
            if p not in custom_state:
                return json.dumps({"error": f"Missing parameter: {p}", "required": PATINA_PARAMETER_NAMES})
        state = custom_state
    elif attractor_id in PATINA_ATTRACTOR_PRESETS:
        attractor_meta = PATINA_ATTRACTOR_PRESETS[attractor_id]
        state = attractor_meta["state"]
    else:
        return json.dumps({
            "error": "Provide attractor_id or custom_state",
            "available_attractors": list(PATINA_ATTRACTOR_PRESETS.keys()),
        })

    # ── Vocabulary extraction ─────────────────────────────────────────
    vtype, vdist = _patina_nearest_visual_type(state)
    vdata = PATINA_VISUAL_TYPES[vtype]
    vocab = _patina_select_vocabulary(state)
    nearest_canon, cdist = _patina_nearest_canonical(state)
    prefix = f"{style_modifier}, " if style_modifier else ""

    # ── COMPOSITE mode ────────────────────────────────────────────────
    if mode == "composite":
        all_keywords = list(vdata["keywords"])
        for cat_terms in vocab.values():
            all_keywords.extend(cat_terms)
        seen = set()
        unique = []
        for kw in all_keywords:
            if kw not in seen:
                seen.add(kw)
                unique.append(kw)
        prompt = prefix + ", ".join(unique)

        return json.dumps({
            "mode": "composite",
            "prompt": prompt,
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
            "nearest_canonical_state": nearest_canon,
            "optical_properties": vdata["optical"],
            "color_associations": vdata["color_associations"],
            "attractor": {
                "id": attractor_id or "custom",
                "name": attractor_meta["name"] if attractor_meta else "Custom State",
                "basin_size": attractor_meta["basin_size"] if attractor_meta else None,
                "classification": attractor_meta["classification"] if attractor_meta else "custom",
            },
            "state": {k: round(v, 4) for k, v in state.items()},
        }, indent=2)

    # ── SPLIT_VIEW mode ───────────────────────────────────────────────
    elif mode == "split_view":
        panels = {}
        for category, terms in vocab.items():
            cat_prompt = prefix + ", ".join(terms)
            panels[category] = {"prompt": cat_prompt, "terms": terms}

        return json.dumps({
            "mode": "split_view",
            "panels": panels,
            "nearest_visual_type": vtype,
            "visual_distance": round(vdist, 4),
            "optical_properties": vdata["optical"],
            "color_associations": vdata["color_associations"],
            "attractor": {
                "id": attractor_id or "custom",
                "name": attractor_meta["name"] if attractor_meta else "Custom State",
                "classification": attractor_meta["classification"] if attractor_meta else "custom",
            },
            "state": {k: round(v, 4) for k, v in state.items()},
        }, indent=2)

    # ── SEQUENCE mode ─────────────────────────────────────────────────
    elif mode == "sequence":
        # Find nearest rhythmic preset by period proximity
        best_preset = None
        best_period_diff = float("inf")
        target_period = None

        if attractor_meta and attractor_meta.get("basin_size"):
            period_str = attractor_id.replace("period_", "")
            try:
                target_period = int(period_str)
            except ValueError:
                target_period = None

        if target_period is None:
            target_period = 30

        for pname, pcfg in PATINA_RHYTHMIC_PRESETS.items():
            diff = abs(pcfg["period"] - target_period)
            if diff < best_period_diff:
                best_period_diff = diff
                best_preset = pname

        cfg = PATINA_RHYTHMIC_PRESETS[best_preset]
        state_a = PATINA_CANONICAL_STATES[cfg["state_a"]]
        state_b = PATINA_CANONICAL_STATES[cfg["state_b"]]
        period = cfg["period"]
        step_size = max(1, period // keyframe_count)

        keyframes = []
        for ki in range(keyframe_count):
            step = (ki * step_size) % period
            t = step / period
            kf_state = _patina_interpolate_states(state_a, state_b, t, cfg["pattern"])
            kf_vtype, kf_vdist = _patina_nearest_visual_type(kf_state)
            kf_vdata = PATINA_VISUAL_TYPES[kf_vtype]
            kf_vocab = _patina_select_vocabulary(kf_state)

            all_kw = list(kf_vdata["keywords"])
            for cat_terms in kf_vocab.values():
                all_kw.extend(cat_terms)
            seen_kf = set()
            unique_kf = []
            for kw in all_kw:
                if kw not in seen_kf:
                    seen_kf.add(kw)
                    unique_kf.append(kw)

            keyframes.append({
                "keyframe": ki,
                "step": step,
                "phase": round(t, 4),
                "prompt": prefix + ", ".join(unique_kf),
                "nearest_visual_type": kf_vtype,
                "visual_distance": round(kf_vdist, 4),
                "state": {k: round(v, 4) for k, v in kf_state.items()},
            })

        return json.dumps({
            "mode": "sequence",
            "preset_used": best_preset,
            "preset_period": period,
            "keyframe_count": keyframe_count,
            "keyframes": keyframes,
            "attractor": {
                "id": attractor_id or "custom",
                "name": attractor_meta["name"] if attractor_meta else "Custom State",
                "classification": attractor_meta["classification"] if attractor_meta else "custom",
            },
        }, indent=2)

    else:
        return json.dumps({"error": f"Unknown mode: {mode}", "available": ["composite", "split_view", "sequence"]})


@mcp.tool()
def generate_patina_sequence_prompts(
    preset_name: str,
    keyframe_count: int = 4,
    style_modifier: str = "",
) -> str:
    """
    Generate keyframe prompts from a Phase 2.6 rhythmic preset.

    Layer 2: Deterministic keyframe extraction (0 tokens).

    Extracts evenly-spaced keyframes from a rhythmic oscillation
    and generates an image prompt for each. Useful for storyboards,
    animation keyframes, and multi-panel visualizations of temporal
    weathering aesthetic evolution.

    Args:
        preset_name: One of the 5 rhythmic presets
        keyframe_count: Number of keyframes to extract (default: 4)
        style_modifier: Optional style prefix for all prompts
    """
    if preset_name not in PATINA_RHYTHMIC_PRESETS:
        return json.dumps({"error": f"Unknown preset: {preset_name}", "available": list(PATINA_RHYTHMIC_PRESETS.keys())})

    cfg = PATINA_RHYTHMIC_PRESETS[preset_name]
    state_a = PATINA_CANONICAL_STATES[cfg["state_a"]]
    state_b = PATINA_CANONICAL_STATES[cfg["state_b"]]
    period = cfg["period"]
    step_size = max(1, period // keyframe_count)
    prefix = f"{style_modifier}, " if style_modifier else ""

    keyframes = []
    for ki in range(keyframe_count):
        step = (ki * step_size) % period
        t = step / period
        kf_state = _patina_interpolate_states(state_a, state_b, t, cfg["pattern"])
        kf_vtype, kf_vdist = _patina_nearest_visual_type(kf_state)
        kf_vdata = PATINA_VISUAL_TYPES[kf_vtype]
        kf_vocab = _patina_select_vocabulary(kf_state)

        all_kw = list(kf_vdata["keywords"])
        for cat_terms in kf_vocab.values():
            all_kw.extend(cat_terms)
        seen = set()
        unique = []
        for kw in all_kw:
            if kw not in seen:
                seen.add(kw)
                unique.append(kw)

        keyframes.append({
            "keyframe": ki,
            "step": step,
            "phase": round(t, 4),
            "prompt": prefix + ", ".join(unique),
            "nearest_visual_type": kf_vtype,
            "visual_distance": round(kf_vdist, 4),
            "state": {k: round(v, 4) for k, v in kf_state.items()},
        })

    return json.dumps({
        "preset": preset_name,
        "period": period,
        "keyframe_count": keyframe_count,
        "keyframes": keyframes,
    }, indent=2)


# ============================================================================
# DOMAIN REGISTRY HELPER
# ============================================================================

@mcp.tool()
def get_patina_domain_registry_config() -> str:
    """
    Get complete domain configuration for emergent attractor discovery.

    Returns the data needed by domain_registry.py to integrate patina
    weathering into the Tier 4D compositional limit cycle discovery system.
    Follows the ADDING_NEW_DOMAINS.md integration pattern.
    """
    registry_presets = {}
    for name, cfg in PATINA_RHYTHMIC_PRESETS.items():
        registry_presets[name] = {
            "name": name,
            "period": cfg["period"],
            "state_a_id": cfg["state_a"],
            "state_b_id": cfg["state_b"],
            "pattern": cfg["pattern"],
            "description": cfg["description"],
        }

    registry_vocab = {}
    for vtype, vdata in PATINA_VISUAL_TYPES.items():
        registry_vocab[vtype] = vdata["keywords"]

    return json.dumps({
        "domain_id": "patina",
        "display_name": "Patina & Weathering",
        "description": "Conservation science weathering aesthetic composition",
        "mcp_server": "patina-weathering-mcp",
        "parameter_names": PATINA_PARAMETER_NAMES,
        "state_coordinates": PATINA_CANONICAL_STATES,
        "presets": registry_presets,
        "vocabulary": registry_vocab,
        "periods": sorted(set(c["period"] for c in PATINA_RHYTHMIC_PRESETS.values())),
        "attractor_presets": {
            aid: {
                "name": adata["name"],
                "basin_size": adata["basin_size"],
                "classification": adata["classification"],
                "state": adata["state"],
            }
            for aid, adata in PATINA_ATTRACTOR_PRESETS.items()
        },
        "domain_registry_ready": True,
    }, indent=2)


# ============================================================================
# SERVER INFO
# ============================================================================

@mcp.tool()
def get_server_info() -> str:
    """
    Get information about the Patina & Weathering MCP server.

    Returns server metadata, architecture overview, Phase 2.6/2.7
    capabilities, and usage guidance.
    """
    return json.dumps({
        "name": "Patina & Weathering MCP",
        "version": "1.0.0-phase2.7+tier4d",
        "architecture": "three_layer_olog",
        "description": (
            "Conservation-science weathering composition with zero-cost enhancement. "
            "Phase 2.6 rhythmic presets for temporal composition, "
            "Phase 2.7 attractor visualization for multi-domain emergence. "
            "Temporal transform — adds a time axis to every material domain."
        ),
        "layers": {
            "layer_1": "Pure taxonomy (materials, agents, condition grades, visual types)",
            "layer_2": (
                "Deterministic mapping (intent classification, parameter selection, "
                "rhythmic presets, trajectory computation, distance, vocabulary, "
                "attractor prompts)"
            ),
            "layer_3": "Claude synthesis interface (structured data for creative composition)",
        },
        "domain_coverage": {
            "material_categories": len(MATERIAL_CATEGORIES),
            "weathering_agents": len(WEATHERING_AGENTS),
            "condition_grades": len(CONDITION_GRADES),
            "canonical_states": len(PATINA_CANONICAL_STATES),
            "visual_types": len(PATINA_VISUAL_TYPES),
            "parameter_dimensions": PATINA_DIMENSIONALITY,
        },
        "phase_2_6_enhancements": {
            "rhythmic_presets": True,
            "preset_count": len(PATINA_RHYTHMIC_PRESETS),
            "periods": sorted(set(c["period"] for c in PATINA_RHYTHMIC_PRESETS.values())),
            "preset_names": list(PATINA_RHYTHMIC_PRESETS.keys()),
            "custom_oscillation": True,
            "trajectory_computation": True,
            "patterns": ["sinusoidal", "triangular", "square"],
        },
        "phase_2_7_enhancements": {
            "attractor_visualization": True,
            "attractor_presets": list(PATINA_ATTRACTOR_PRESETS.keys()),
            "prompt_modes": ["composite", "split_view", "sequence"],
            "visual_vocabulary": True,
            "domain_registry_ready": True,
        },
        "science_foundation": [
            "Conservation science condition assessment",
            "Materials engineering degradation mechanisms",
            "Geological weathering processes",
            "Archaeological stratigraphy",
            "Wabi-sabi aesthetic philosophy",
        ],
        "aesthetic_applications": [
            "Architectural photography (patinated surfaces)",
            "Still life (antique objects)",
            "Concept art (post-apocalyptic, ruins)",
            "Product design (intentional aging, Corten steel)",
            "Museum/conservation documentation",
            "Historical reconstruction (period-accurate wear)",
        ],
        "functorial_connections": [
            "Material base → surface design domains (temporal transform)",
            "Condition grade → catastrophe theory phase transitions",
            "Biological colonization → diatom/microscopy aesthetics",
            "Color transformation → stage lighting interaction",
            "Structural integrity → splash/deformation dynamics",
        ],
        "compatible_servers": [
            "catastrophe-morph-mcp",
            "diatom-morphology-mcp",
            "surface-design-aesthetics",
            "microscopy-aesthetics-mcp",
            "stage-lighting-mcp",
            "splash-aesthetics-mcp",
            "aesthetic-dynamics-core",
            "composition-graph-mcp",
        ],
        "cost_model": "0 tokens for Layers 1-2, creative synthesis by Claude at Layer 3",
    }, indent=2)


if __name__ == "__main__":
    mcp.run()
