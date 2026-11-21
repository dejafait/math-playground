# Fixed neutral U6 scalar-floor family: audited stop

WHY IT FAILS: [C750c](../lemmas/C750c-fixed-neutral-scalar-floor-schur-rejection.md)
uses the fixed U12 compression to force any positive complementary
floor below .001 while a different complementary direction supplies
enough lower cross covariance to make the retained scalar-certificate
value less than -1.282. Hence proving a positive full floor and paying
all covariance cannot rescue this sufficient family for the unchanged
U6 split. This is not a negative complete Weil form: the low-energy
trial's interval contains zero. Exact inverse Schur elimination,
different splits and RH remain unresolved. Step872 left the conclusion
pending a separate critical audit; no sweep was made.

Audit873 now accepts the stop under the stated IEEE arithmetic model:
both complete replays match and all37 domain/coordinate/accounting
checks pass. See C750c Proof4 for the full argument and artifact paths.
No sign of E(z) or obstruction to exact inverse Schur theory follows.
