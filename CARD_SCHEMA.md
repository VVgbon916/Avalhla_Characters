# CARD SCHEMA

Cards are derived views.

## 01 / PURPOSE

A card can present:

- mapped statistics
- colors and symbols
- equipment
- abilities or skills
- relationships
- history
- visual presentation

None becomes canonical merely because it appears on a card.

## 02 / REQUIRED IDENTITY

`text
card_id
source_concept_id
canonical_name
view_type
presentation
generated_at
`

## 03 / SOURCE RULE

A card must point back to one canonical source record.

A card cannot become the source of a new `concept_id`.

## 04 / MAPPING RULE

Mappings used by a card remain explicitly named and separate from canonical attributes.

## 05 / VISUAL RULE

Visual composition may be expressive.
Visual geometry may carry story.
Visual geometry does not redefine identity or authority.
