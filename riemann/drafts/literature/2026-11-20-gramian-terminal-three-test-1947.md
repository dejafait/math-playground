# Fixed-horizon dynamical Gramian: proposed test1947

TARGET: Test whether the d^2-horizon coefficient Gramian removes the centered-companion terminal-three floor by establishing r_d=o(1), or a positive liminf, for the exact r_d defined in assessment1947.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Discovery1947 searched exact Jensen/finite-horizon Gramian, companion/Gramian/commutator, and approximate-symmetrizer terminology, compared C028h/i/o/p and stops1525/1588/1695/1713 plus audited C029a, and found no matching actual-family terminal-three estimate. Full search scope and exclusions are in source-notes1947; no novelty is inferred.
SOURCE_EVIDENCE: Stillfjord-Tronarp arXiv2310.13462v2 Section1 (1b)-(2) p1 and Section1.2 (5) p4 https://arxiv.org/pdf/2310.13462v2 ; Redmann-Kürschner 2July2018 Lemma2.1/full proof/remark pp5-6 https://pure.mpg.de/rest/items/item_2491617_13/component/file_2630664/content ; reuse Schmeisser2002 Lemma1 pp211-212 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf and Watrous2018 Section1.1 pp32-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf under assessment1523. Source-notes1947 records hypotheses and read proof cases.
COMPARISON: Finite-horizon integrals provide a coefficient-defined positive metric without a stability or real-root premise; existing matrix inputs cover full-height upper majorants and orthogonal compression. They do not estimate this increasing-degree dynamical metric or its inverse. Nishitani2004.03825v2's hyperbolic quasi-symmetrizers cannot provide the missing positivity for the actual family. No old diagonal/shear/theta floor is imported for G_d.
GAP: Neither r_d=o(1), a positive liminf, uniform conditioning nor any full-cost estimate is established. The normalized compression must be justified in the research attempt before its asymptotic is used. Vanishing compression would leave the complete trace norm and H_d=o(d) unresolved.
REASON: The discovery target has produced one concrete construction and a discriminating central test with finite-source coverage. The d^2-horizon actual-coefficient asymptotic is not supplied by the inspected theorems. This newly written assessment requires separate approval before research; no estimate was derived or approved during discovery1947.
SCOPE: Exactly C028h's actual centered companion, integers d>=3, fixed D_d and T_d below, full finite-horizon integral and its specified three-coordinate energy compression. No fitted roots, real/simple spectrum, bounded conditioning, spectral separation, unknown symmetrizer or effective numerical contract is assumed.

## Exact proposed objects

These are test definitions, not asserted new estimates. Use the actual
P_d,Q_d,A_d of C028b/d/h, including every coefficient and algebraic
multiplicity. Fix, in the indicated order,

    D_d=diag(1,d,d^2,...,d^(d-1)),
    C_d=(1/d) D_d A_d D_d^(-1),
    M_d=[0 -C_d; C_d 0]  (a real 2d by 2d matrix),
    T_d=d^2,
    W_d=integral_0^(T_d) exp(t M_d^T) exp(t M_d) dt,
    G_d=(1/T_d) times the upper-left d by d block of W_d.

This is the source's finite-horizon controllability Gramian for
generator M_d^T and identity input, equivalently its observability
version. Identity input verifies controllability immediately; the
positive principal block yields a real positive definite G_d in each
finite degree. No infinite-time integral or algebraic Lyapunov inverse
is used. All coefficients enter before the block is taken. There is no
truncation of the actual polynomial to its last three coefficients.
The construction is unrestricted by a Hankel moment ansatz; no claim
of non-Hankel structure in every degree is required.

Let E_d include the last three coordinate vectors in R^d, in their
original order, and put

    Gamma_d=E_d^T G_d E_d,
    R_d=Gamma_d^(-1/2) E_d^T (G_d C_d-C_d^T G_d) E_d
                        Gamma_d^(-1/2)/(2i),
    r_d=||R_d||_1.

Square roots are the positive definite symmetric ones; ||.||_1 is the
Schatten trace norm. R_d is a complex Hermitian three by three matrix.
It is a compression in the G_d inner product, not the old Euclidean
terminal block of C_d. In the attempt, verify its relationship to the
full transformed skew matrix using the isometry
G_d^(1/2) E_d Gamma_d^(-1/2). Do not apply C028h's diagonal formula
after this full mixing, or regard r_d as the complete trace norm.

## One bounded mathematical attempt after separate approval

Seek an analytic all-degree asymptotic or uniform estimate for this
single r_d sequence, with the horizon and metric fixed. The desired
escape threshold is r_d=o(1). A proved liminf r_d>0 is the decisive
obstruction test and stops this metric schedule as an o(d) payment.
If neither is justified, preserve the incomplete estimates and name
the missing uniform bound; do not silently replace d^2 by another
horizon or fit a different metric. Finite values alone settle neither
asymptotic alternative. No mathematical program is prescribed.

The downstream full-cost target, not a premise, is

    k_d=||(G_d^(1/2) C_d G_d^(-1/2)
                -G_d^(-1/2) C_d^T G_d^(1/2))/(2i)||_1=o(1).

The attempt must justify the standard compression and Schmeisser
specializations with the scale d before using r_d<=k_d and
H_d/d<=k_d. A positive compression floor is only a lower bound on
this upper majorant, not on H_d. If r_d=o(1), full-cost control remains
independently open. Actual coefficient uniformity and possibly severe
energy-metric conditioning may prevent either test from closing.
The d^2 horizon is a fixed exploratory choice allowing propagation
through all coordinates, with no asserted source guarantee of success.

Use C028h's exact centered coefficients, C028b's actual height criterion
and the ready general matrix inputs. C028h/i/o/p and C029a are contrast
evidence only. C028c/L778 and the retained Decimal/backend contracts
become essential if their numerical coefficient enclosures are used;
none is newly attested. Full matching Mathlib coverage is unchecked.

Creative routing is for the degree-dependent dynamical-energy
asymptotic, not for reproving Gramian positivity or a norm inequality.
The bounded decisive evidence is a vanishing r_d bound or a fixed
positive liminf for this exact schedule. No complete RH candidate is
claimed. Any unresolved tail or normalization estimate must survive
in the continuation record.
