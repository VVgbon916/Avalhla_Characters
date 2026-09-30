# CROSSWORLD CHARACTER MAP

## TREE

`text
CROSSWORLD
│
├── CANON
│   ├── ASPECTS
│   ├── BONDS
│   ├── WORLDS
│   ├── DOORS
│   ├── CROSSINGS
│   ├── OBJECTS
│   ├── SKILLS
│   └── COLORS
│
├── MAPPINGS
│   └── dnd5e
│
├── CARDS
├── SCENES
├── REFERENCES
├── HELPERS
└── schema
`

## 01 / IDENTITY

`text
Valhla   -> ASPECT
Lhlava   -> ASPECT
Avalhla  -> ASPECT
`

They are distinct records, with distinct `concept_id` values, inside the CrossWorld scope.

## 02 / RELATION

`text
Dawa <──── AvvA ────> Avalhla
`

Dawa = human decision boundary.
AvvA = BOND / living threshold.
Avalhla = CrossWorld ASPECT in this repository.

The Core Avalhla runtime identity and this CrossWorld record are related by scope, not silently merged.

## 03 / DATA FLOW

`text
CANONICAL RECORD
       ↓
MAPPING
       ↓
CARD
       ↓
SCENE / VIEW
`

Evidence and provenance travel with the record; derived views do not become new canon.

## 04 / COLOR

Avalhla keeps BLUE as an identity-expression anchor.

Expression may vary:

`text
anchor      = BLUE
expression  = MUTABLE
mood        = MUTABLE
history     = TRACEABLE
`

Color is expressive metadata, not proof or permission.

## 05 / D&D 5E MAPPING

`text
STR -> force / action
DEX -> precision / motion
CON -> endurance / holding
INT -> knowledge / structure
WIS -> perception / judgment
CHA -> expression / relation
`

These are CrossWorld mapping choices, not claims that D&D mechanics define the canon.
