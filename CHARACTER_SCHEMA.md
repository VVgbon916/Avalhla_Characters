# CHARACTER SCHEMA

The machine contract lives in `schema/crossworld-record.schema.json`.

## 01 / REQUIRED IDENTITY

Each canonical record has:

`text
record_type
concept_id
canonical_name
scope
status
description
`

`concept_id` is the stable identity anchor.

Changing presentation or adding an alias does not create a new identity.

## 02 / NAMES

`canonical_name` = one preferred human name inside the declared scope.

`aliases` = historical, colloquial, or compatibility names.

Aliases never become competing canonical artifacts.

## 03 / RELATIONS

Relations point to other `concept_id` values.

A BOND is a record in its own right and may contain participants plus a canonical relation signature.

A relation does not grant agency or authority.

## 04 / MAPPINGS

Mappings are separate from canon.

A mapping may describe a D&D 5e interpretation without importing D&D semantics into the source record.

## 05 / PROVENANCE

Provenance records where the record came from.

The repository does not pretend a human design decision is an external fact.

The initial three ASPECT records therefore identify their source as the CrossWorld design contract rather than fabricating outside evidence.

## 06 / INTEGRITY

SHA-256 is exact-byte identity/evidence.

It does not prove meaning, truth, authority, permission, or semantic similarity.

Self-referential record hashes are not required by the base schema; a future integrity process may calculate them externally.
