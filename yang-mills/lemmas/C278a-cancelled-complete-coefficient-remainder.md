# C278a — Conditional remainder after complete cubic cancellation

## Hypotheses

Assume the full analytic hypotheses of L220 and L278 simultaneously,
including their imported estimates, analytic identities, absolute
convergence and recorded audit qualifications. Neither input nor its
upstream premises is recursively verified here. Use exactly L011(6)'s
bare fixed-mesh coefficient Gamma_(i,a) and L218(2)'s mathcal L_i.

Keep SU(2), the all-face relative cube (-4,4)^4, admitted sufficiently
large even N, a=8/N, tau=1/16, the straight lower-rooted direction-1
forest, ordinary stored coordinates, the unchanged compact displacement
and both actual probes i=3,6. Take the bare small-coupling coefficient
at fixed mesh before refinement. Preserve three colors, both residual
subtractions and forms/orientations, all source and normal/end rows,
upper pin/jump, allowed constant component indices, ordered plaquette
pairs, constant axial prefix and full physical heat sums.

In particular retain L220's analytic scalar identities and its common
physical-form normalization, and all complete estimates required by
L278. No numerical enclosure, IEEE arithmetic or diagnostic sign
premise is required. This is an implication from the union of these
premises, not a proof that all imported analytic estimates hold.

## Conclusion

There are finite nonnegative constants C_i and a common threshold N_0,
independent of N, such that for i=3,6 and every admitted even N>=N_0,

    |Gamma_(i,a)| <= C_i N^(5/2)log(eN)^2.                 (1)

Equivalently,

    |a^3 Gamma_(i,a)| <= 512 C_i N^(-1/2)log(eN)^2.       (2)

The constants and mesh threshold may be taken from L278, restricted
to the same fixed data and the union of premises above. This is local
RESEARCH / REPRODUCTION of a conditional consequence of recorded
inputs; no progress beyond the checked sources is claimed. It is
neither a new analytic estimate nor an O(N^2) bound. No claim about
the signed leading remainder, finite matching, cutoff-uniform coupling
expansion, interacting reflection positivity, nonzero physical sector,
continuum axioms or infinite-volume positive mass follows. This is
not a complete Yang--Mills candidate.

## Proof

The prior SPECIALIZE assessment
`drafts/literature/2026-10-25-cancellation-remainder-compatibility.md`
approves exactly this finite application. L278(2) defines

    mathcal L_i=P_i+A_i^dm+Lambda_i+K_(i,T)+K_(i,Vmix)
                         -6K_(i,R)+3K_(i,oo)+12 gamma D_i.

This is literally L218(2), which L220's hypotheses identify as its
complete coefficient. L219's contraction used inside L220 rewrites
this same quantity; it does not replace it with a selected group.
The signs, the outside three and the diagnostic factor 12 are unchanged.
The fixed cube, mesh family, forest, flow time, displacement, probes
and bare-first order agree. L278's additional row/orientation and
complete-bound requirements remain hypotheses, as do L220's scalar
identities and absolute convergence. Thus no domain, normalization
or limit premise is dropped in using the two statements together.

Under these assumptions L220(1) gives mathcal L_i=0 for each actual
probe. On L278's common admitted mesh range its (1) therefore reads

    |Gamma_(i,a)|
      =|Gamma_(i,a)-a^(-3)mathcal L_i|
      <= C_i N^(5/2)log(eN)^2,

which proves (1). Cancellation is substituted into the signed
coefficient-subtracted expression before taking its magnitude; no
separate absolute group estimate is substituted for a signed identity.
Since a^3=512/N^3 is positive, multiplication proves (2). No limit
interchange, new infinite-sum rearrangement or mesh-dependent choice
of a fixed-mass constant occurs. ATTEMPTS/030 and ATTEMPTS/032 are
not reopened: neither shortcut is used by this implication.

Only canonical L220(1) and L278(1)--(2) are applied. Their full proofs
and separate conditional audits remain canonical; no external theorem
is newly applied or reproved. The primary-source comparisons and their
limits are retained in the ready assessment. The displayed upper
bound grows with N and supplies no cutoff-uniform interacting control.
In particular its N^(5/2)log(eN)^2 allowance cannot be relabeled O(N^2).

### Separate critical audit — 2026-10-25

Audit YM-20261025-475-cancelled-corollary-critical-audit, under the
prior SPECIALIZE assessment
`drafts/literature/2026-10-25-cancelled-coefficient-corollary-critical-audit.md`,
accepts (1)--(2) without correction, conditional on the full union of
the two inputs' premises. This is RESEARCH / REPRODUCTION verification
of a finite implication, not a new estimate or an upstream analytic
verification. The following checks use the canonical statements and
their recorded audit dispositions; they do not infer correctness from
the fact that earlier audits were recorded.

**Objects and premises.** L220's opening hypothesis identifies its
complete coefficient with L218's coefficient of L011(6). L278's opening
hypothesis makes the identical identification, and its (2) is exactly
the eight-term expression displayed above: the residual R coefficient
is -6, the other/other coefficient is +3, and the diagnostic coefficient
is +12 gamma. L220(1) sets this complete coefficient to zero, not just
its selected-group contraction. Both statements use the same fixed
SU(2) cube, lower-rooted forest, flow time, probes, mesh family and
bare-first order. No disputed identification calls for reopening
L218/L219.

The hypothesis "full analytic hypotheses ... simultaneously" retains
L220's imported existence limits, L219 normalization and audit scope,
exact scalar identities and absolutely convergent full physical forms.
It also retains L278's exact group conventions, all complete bounds,
centered mixed trace with its exterior defect, diagnostic comparison
and boundary/source conditions. In particular a cancellation theorem
does not discharge a bound's analytic premises. The proof uses only
these stated implications; consistency or independent validity of all
their upstream estimates is not proved here. L220 excludes numerical
enclosures from this cancellation, and L278 uses analytic finiteness,
not a numerical sign, so C278a introduces no omitted numerical premise.

**Quantifiers and common range.** Fix all the shared data and assume
that union. L278 provides mesh-independent finite constants and one
threshold for both probes. Its proof constructs nonnegative constants
as finite sums of allowances, so the nonnegativity in C278a is allowed.
Restrict to the admitted even meshes above that threshold. L220's
identity mathcal L_i=0 is an identity of the limiting coefficient for
these fixed data; it is not an approximation requiring a further
mesh-dependent tolerance or threshold. Thus L278's constants and
threshold apply on this same range. Dependence on fixed data is
permitted; uniformity in displacement, coupling or volume is not asserted.

**Substitution and scaling.** For each of the two probes and every
mesh in that range, substitute L220(1) into the single signed difference
in L278(1). This gives exactly |Gamma_(i,a)| on its left side and leaves
its right side unchanged. This step neither bounds separately the
canceling terms nor interchanges limits. Since N>0 and a=8/N,
a^3=8^3/N^3=512/N^3>0 and |a^3 Gamma|=a^3|Gamma|.
The resulting exponent is 5/2-3=-1/2, proving (2); conversely division
by this positive factor recovers (1). No additional factor of three,
six, or covariance normalization occurs.

**Limit of the verdict.** The unscaled allowance remains
N^(5/2)log(eN)^2, not N^2. The audit does not bound a remainder in the
coupling expansion or identify Gamma with a centered reflection norm.
ATTEMPTS/030's mesh-dependent use of a fixed-mass constant and
ATTEMPTS/032's separate absolute-moment shortcut are not used.
No polynomial or numerical certificate is needed for this substitution;
none has been replayed or newly certified. The direct mathematical
inputs remain L220 and L278, so no DAG change is needed. The main
interacting, continuum and infinite-volume mass gaps remain open.

## Mathlib

Full specialized conditional forest-coefficient consequence: **not
checked**. Supporting substitution of a zero scalar and multiplication
of inequalities by positive scalars: **not checked**. No Mathlib
declaration is used to verify the upstream analytic premises; unknown
coverage is not absence.
