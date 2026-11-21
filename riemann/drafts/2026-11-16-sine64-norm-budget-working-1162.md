# Fixed sine64 norm-budget attempt1162 (working)

Approved target: assessment1160, unchanged SPECIALIZE scope. Main gap:
L030-L032/C032a actual-Xi positivity. Attempt only the prescribed norm
budget, no head assembly or retuning. Relevant normalization: L744(6),(8),
C750f's complete complex form. Zhu v2(4), Lemma6.1, (13),(16) inspected.
Prior1159/1160 comparison and signed-localization583/584 stops reused.

Possible decisive test, not yet established: take an odd sine index n>64
with alpha=n*pi/(2b) between T/4 and T/2. This is a witness in the
UNCHANGED complement, not an enlarged head. Its pole is nonnegative.
The exact full correlation should be
R_phi(u)=(1-u/(2b))*cos(alpha*u)+sin(alpha*u)/(2b*alpha).
Thus the full comb costs at most A-D+A/(2b*alpha), where
D=sum c_n*log(n)/(2b). The17 primes23,...,97 alone suggest D>6.12.
The exact sine transform bounds low-frequency leakage by1/alpha and
the frequency tail beyond T by1/T. These may give <K phi,phi>>2,
forcing every admissible delta above beta<2 independently of coupling.
All inequalities, constants, complex kernel and closed-domain comparison
still require complete checking. No mathematical result is claimed here.

If proved, retire the two-sided norm certificate only. A positive
complement witness is neither a negative Weil direction nor failure
of a one-sided lower enclosure. Save full proof canonically and propose
a separate conceptual audit; do not approve that new assessment this turn.

Completed1162: the proposed witness and full applicability argument
are now proved in canonical C750m, with <K phi,phi>>200269/50000>4
and beta<2. The proof remains pending independent conceptual audit.
The9 exact arithmetic checks pass; they do not audit the analysis.
The earlier tentative text is preserved as working history only.
