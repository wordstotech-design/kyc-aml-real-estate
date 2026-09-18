# KYC AML Real Estate

<p align="center">
  <a href="https://www.idenfy.com/">
  <img width="1657" height="937" alt="image" src="https://github.com/user-attachments/assets/06307815-2fd6-439c-a5d6-cb7427a6b32c" />


  </a>
</p>

A house does not ask where the money came from. That is precisely why criminals prefer it to a bank account, and why running [KYC for real estate agencies](https://www.idenfy.com/kyc-software/) has stopped being optional in most of the countries where property changes hands for six or seven figures. A wire transfer trips a bank's monitoring system in seconds. A cash purchase routed through a company nobody has heard of, closed by a title agent who never asks who actually owns that company, trips nothing at all.

This repository maps where identity checks belong across a property transaction, summarizes what regulators in the US, Canada, and the EU currently require, and compares the KYC platforms real estate firms actually use to run those checks. [tools.yaml](tools.yaml) holds the provider data and [render_table.py](render_table.py) rebuilds the table below from it, so the two cannot quietly drift apart.

## Why real estate keeps showing up in money laundering cases

Real estate solves three problems for someone moving illicit funds at once. A cash purchase avoids the financial institution that would otherwise file a suspicious activity report. A trust or a shell company sits between the buyer's name and the county land registry, so the true owner never appears on a public document. And because property values move, a launderer can sell a house at a price that has nothing to do with what it is worth, turning dirty money into a clean profit on paper.

Four patterns account for most of what investigators actually find:

- **Large cash purchases.** Structuring a purchase to sit under a reporting threshold, or splitting it across several smaller transactions, so no single payment draws attention.
- **Ownership hidden behind a company or a trust.** The buyer of record is a legal entity, and the person who controls it, the beneficial owner, is never named on the deed.
- **Flipping with no real work done.** A property bought and resold quickly at a higher price, with little or no renovation to justify the markup.
- **Payment through an unusual channel.** Cryptocurrency, an offshore account, or a private lender standing in for a bank that would otherwise ask questions.

None of these four is illegal by itself. A cash buyer, a trust, a quick resale, and a crypto payment all have entirely legitimate uses. What makes them worth flagging is when two or three show up on the same file, which is exactly the pattern a KYC and AML program is built to catch.

## Where the legal obligation actually sits right now

Obligations here are not static, and the United States is mid change as of this writing.

**United States.** From 2016 onward, FinCEN ran Geographic Targeting Orders (GTOs) requiring title insurance companies to identify the natural person behind a shell company buying property with cash, but only in a defined list of metro areas above a purchase price threshold. FinCEN finalized a nationwide Residential Real Estate Rule meant to replace the GTOs with nationwide, threshold free reporting, and the GTOs were renewed once more on October 9, 2025 as a bridge until that rule took effect on March 1, 2026. On March 19, 2026, a federal court in the Eastern District of Texas vacated the rule, and FinCEN has confirmed that reporting persons are not currently required to file under it while that order stands and its appeal to the Fifth Circuit is pending. See [FinCEN's residential real estate FAQ](https://www.fincen.gov/rre-faqs) for the current status and [the GTO renewal notice](https://www.fincen.gov/news/news-releases/fincen-renews-residential-real-estate-geographic-targeting-orders-0) for what the GTOs still cover in the meantime. Confirm the live status before telling a client either rule is or is not in force.

**Canada.** FINTRAC found in 2018 that a number of real estate businesses were not meeting their AML obligations, some by design. Canada responded in 2021 by making politically exposed person (PEP) checks and beneficial ownership identification mandatory for reporting entities, real estate professionals included.

**European Union.** The fourth AML Directive brought real estate agents under EU AML law in 2018, with KYC verification as a baseline requirement. The sixth directive extended liability from the individual agent to the entire firm, so a single agent helping overvalue a property can now expose the whole business to sanctions.

None of this makes iDenfy, or any other vendor named below, a compliance program on its own. A real estate business stays the obliged entity under whichever of these rules applies to it. A verification platform supplies the identity layer that program runs on.

## KYC checkpoints across a real estate deal

A transaction gives a business four separate moments to check who it is actually dealing with, and each one catches a different kind of problem.

**Offer accepted.** This is where basic KYC happens, full legal name, date of birth, current address, and a government issued document for every individual named on the offer. If the buyer of record is a company or a trust rather than a person, this is also the point to start [business verification for real estate](https://www.idenfy.com/know-your-business-solution/) rather than treating the entity as if it were an individual buyer.

**Due diligence and escrow.** Before funds move, run sanctions and PEP screening against every named party, plus adverse media checks for public reporting tied to fraud or corruption. If the buyer is an entity, this is where beneficial ownership gets identified, tracing through the company to the person who owns more than 25 percent of it or otherwise controls it. A [KYB guide worth reading in full](https://www.idenfy.com/blog/know-your-business-kyb/) covers how that ownership trace actually works.

**Closing.** Source of funds gets documented here, not assumed. A cash purchase, an unusual payment method such as cryptocurrency, or a buyer based in a jurisdiction with weak AML enforcement each raise the bar for what documentation is enough before the deal proceeds. [PEPs and sanctions checks](https://www.idenfy.com/blog/peps-and-sanctions-checks/) explains what a match at this stage actually requires a business to do next.

**After closing.** Ownership records and watchlists change after the deal is done, not just before it. A reporting business with an ongoing relationship to the property, a management company, or a repeat buyer needs a trigger to reverify rather than treating the initial check as permanent.

Skipping any one of these four checkpoints is how a file that looks clean on the surface turns into the kind of case a regulator asks about a year later.

## Best real estate KYC tools

Every platform below documents business verification, beneficial ownership screening, or both, since a real estate deal involving an entity buyer needs one or the other and often needs both. Rates and features are dated per row because vendor pricing pages change.

<!-- TABLE:START -->
| Provider | KYB and UBO checks | AML screening | Billing model | Best for |
| --- | --- | --- | --- | --- |
| [iDenfy](https://www.idenfy.com) | KYB Business Verification identifies beneficial owners holding more than 25 percent of a company, bundled with individual KYC in the same account | Sanctions and PEP screening, plus AML ongoing monitoring on Enterprise | From 1.35 EUR per verification, 135 EUR monthly minimum. Approved only billing is a 0.50 EUR add on, as of September 2026 | Brokerages that want KYC, KYB with UBO checks, and AML screening under one contract instead of three separate vendors |
| Trulioo | GlobalGateway draws on 700 plus data sources for business verification, the deepest UBO data of this group, though individual KYC is a lighter part of the product than in a dedicated IDV vendor | Not itemized as a standalone line in public materials | Custom, volume based, sales led. Rates not publicly disclosed as of May 2026 | Title and escrow companies that need the deepest beneficial ownership data on a buyer hiding behind a shell company |
| Sumsub | KYB module covers company and UBO checks, configured through a visual workflow builder so rules can vary by state or country without engineering support | Sanctions, PEP, and adverse media screening included in its stack | 1.35 to 1.85 USD per verification, 149 to 299 USD monthly minimum, as of May 2026 | Brokerages onboarding buyers across many states or countries that need to change KYC and AML rules per jurisdiction often |
| Veriff | Added KYB and UBO checks in house after acquiring Vespia in February 2026, closing a gap it previously covered through a partner | Sanctions and PEP screening available, historically sold as an add on | 0.80 to 1.89 USD per completed verification, 49 to 209 USD monthly minimum, as of May 2026. Bills a completed session whether or not it is approved | Firms whose buyers present unusual or non Latin script documents, since Veriff covers more than 12,500 document types |
| Ondato | Runs business onboarding for named banking customers Luminor, SEB, and Swedbank, though public materials do not break out UBO screening as its own line item | Bundled, but reporters note it requires manual activation per customer rather than switching on by default | Subscription plus per verification, roughly 0.50 to 1.40 EUR, as of May 2026 | A brokerage already inside a bank's vendor stack, since three named regional banks already run onboarding on Ondato |
<!-- TABLE:END -->

**iDenfy** covers the full path in one account, individual KYC, KYB with UBO identification, and sanctions or PEP screening, audited under ISO/IEC 27001:2022 and SOC 2 Type II. See [iDenfy's pricing](https://www.idenfy.com/pricing-plans-v3/) for the current per verification rates and add on costs, and [iDenfy's security page](https://www.idenfy.com/security/) for the full audit list. Note that approved only billing now runs as an add on rather than the default, a change worth checking against your own approval rate before assuming it is the cheaper option.

**Trulioo** is the deepest option here specifically for beneficial ownership data, built on a business verification network few competitors match. It is the right call for a title or escrow company whose whole job is confirming who is actually behind the entity on the deed, and the wrong call for a brokerage that mainly needs fast individual KYC at the offer stage.

**Sumsub, Veriff, and Ondato** each cover KYB and UBO checks to varying degrees, and each makes sense in a specific setup: Sumsub where onboarding rules need to flex by jurisdiction often, Veriff where buyers present document types outside the common set, and Ondato where a brokerage is already working inside a bank's existing vendor relationship.

## How to choose

**A brokerage handling individual buyers most of the time** needs fast document based KYC more than deep UBO data. iDenfy or Veriff both fit, with the choice coming down to document coverage for your buyer pool and whether approved only billing matters to your volume.

**A title or escrow company closing deals for shell companies and trusts** should weight beneficial ownership depth over speed. Trulioo's data network or iDenfy's KYB module both name the person controlling the entity, which is the actual deliverable a compliance file needs.

**A developer or property manager with an ongoing buyer relationship** needs reverification triggers more than a one time check, since ownership and watchlist status both change after closing. Confirm any platform's ongoing monitoring option before assuming a single initial screen covers the life of the relationship.

## FAQ

### Why is real estate so exposed to money laundering compared to other assets?

A property transaction can involve cash, an entity buyer, and a resale, three things a bank account rarely combines in one transaction. Each one independently is normal. Together, and repeated across a portfolio, they are the pattern investigators look for.

### What is the difference between KYC and KYB in a real estate transaction?

KYC verifies an individual, full name, date of birth, address, and a government issued document. KYB verifies a business, confirming it is a real, registered entity and identifying the people who own or control it. A real estate deal needs KYC when the buyer is a person and KYB, including UBO identification, when the buyer is a company or a trust.

### Does a small brokerage actually need dedicated KYC software?

A spreadsheet and a photocopy of an ID satisfy nobody once a regulator asks to see the file. A small brokerage handling even a handful of entity buyers a year already has the risk profile that a dedicated platform, rather than a manual process, is built to cover.

### Is the US FinCEN Residential Real Estate Rule currently in effect?

No, not as of this writing. A federal court vacated the rule on March 19, 2026, and FinCEN has stated reporting persons are not required to file under it while that order remains in force. The prior Geographic Targeting Orders in specific metro areas were renewed as a bridge before the vacated rule was due to replace them. Confirm the live status on [FinCEN's own FAQ page](https://www.fincen.gov/rre-faqs) before relying on either rule.

### How does iDenfy help a real estate business meet its AML obligations?

iDenfy provides the verification layer, individual KYC, KYB with beneficial ownership identification, and sanctions or PEP screening, that a real estate business's own AML program runs on. The business remains the obliged entity under whichever rule applies to it. iDenfy is audited under ISO/IEC 27001:2022 and SOC 2 Type II rather than licensed or approved by any regulator, and neither iDenfy nor this repository is a substitute for advice from counsel on your specific obligations.

## Contributing and credits

To correct a fact, add a provider, or update a rate, edit [tools.yaml](tools.yaml), run `python render_table.py --write`, and open a pull request per [CONTRIBUTING.md](CONTRIBUTING.md). The regulatory framing here is adapted from iDenfy's [KYC in real estate guide](https://www.idenfy.com/blog/kyc-aml-real-estate/), the publisher of the source article and the top ranked provider in the table above. The transaction stage structure, the FinCEN status update, and the provider writeups are independent of that source. Nothing here is legal advice. Confirm your own obligations with counsel.

## License

MIT. See [LICENSE](LICENSE).
