# Contributing

This repository maps KYC and AML checkpoints across a real estate transaction and compares the platforms that run those checks. Corrections and additions are welcome.

## Edit the data, not the table

1. Edit [tools.yaml](tools.yaml). Each provider needs `name`, `url` (optional, competitor rows stay unlinked), `kyb_and_ubo`, `aml_screening`, `billing_model`, and `best_for`.
2. Run `python render_table.py --write` to regenerate the block between the `<!-- TABLE:START -->` and `<!-- TABLE:END -->` markers, or `python render_table.py --check` to confirm the two are already in sync.
3. Open a PR and link a source for any rate, feature, or ownership claim.

## What gets merged

- A `billing_model` change backed by the provider's own current pricing page, dated.
- A `kyb_and_ubo` or `aml_screening` change backed by the provider's own documentation, not a sales page adjective.
- A `best_for` naming the buyer and the constraint that makes this provider the right fit, not an adjective.
- A regulatory status correction backed by a primary regulator source, such as FinCEN, FINTRAC, or an EU directive text.

## What gets rejected

- A review platform score column. Review platforms are a business's own customers rating it, not a neutral capability check.
- Affiliate links. Provider domain only, and only for the provider that publishes the source data.
- Duplicate rows. Update the existing entry.
- Legal advice framed as settled when a rule's status is actually in dispute or under appeal.

## Setup

```bash
pip install pyyaml
python render_table.py          # preview
python render_table.py --write  # write into README.md
python render_table.py --check  # verify README already matches tools.yaml
```
