# Lemma 780: an actual negative eliminated block in the balanced Schur test

## Hypotheses

Use L776/L777's actual function G(w)=xi(1/2+sqrt(w)/2)/8 and the
independently certified pair r=3, k=2, R=2048 of L779. Retain L779's
analytic and arithmetic contracts and its step439 audit qualifications.
In particular, the exact interior zeros alpha1,alpha2 are distinct,
real, simple and negative; they exhaust the interior zeros; F=G(Rz)/P
is entire and zero-free on a neighborhood of |z|<=9/8. These are
fixed-pair conclusions of L779, not global real-zero assumptions.

For P(z)=(z-alpha1)(z-alpha2), p=z^-2 P, take the exact linked factors
b=p/F and c=F/p. Let d1,d2 be the complete residues of c at the nodes,
v(alpha)=(1,alpha,alpha^2,...)^T, V=(v(alpha1),v(alpha2)), and

    C=diag(d1,d2), U=Q3 H(b)V, Y=Q3 V, S=Y^T U.

L779 certifies d1>0>d2. In this lemma W means diag(sqrt(|d1|),
sqrt(|d2|)), not L777's conjugate-column matrix. Set

    J=diag(1,-1), B=W S W, M=I-J B,
    B0=(B+B^T)/2, M0=I-J B0, H(X)=(X+X^T)/2.

Order by positive then negative residue and define the scalar eliminated
blocks D=M22 and D0=(M0)22. No positive-block assumption is made.

## Conclusion

The actual blocks satisfy the rigorous bounds

    -0.0007617242877 < D=D0 < -0.0007617242869 < 0.       (1)

Thus both required coercivity conditions lambda_min H(D)>0 and
lambda_min H(D0)>0 of the approved Schur-defect test fail on its fixed
actual-Xi benchmark. Both blocks are nevertheless invertible, with
|D^-1|=|D0^-1|<1313. The true Schur complement T of D is also negative:
det(M)=D T>0 by L779, so T<0. No value or sign of the reference Schur
complement T0 is needed or asserted.

This is a fixed-pair obstruction to the specified positive-block
certificate. It neither disproves an exceptional minor nor rules out
indefinite inertia arguments, other normalizations or eventual estimates
that explicitly exclude this pair. No growing-order bound or RH claim
is made. The new scalar transfer has not received a later independent
audit; it inherits the audited input's software/analytic qualifications.

## Proof

**Imported interfaces and the exact balancing.** Reuse the source
coverage in `drafts/literature/2026-11-04-balanced-schur-defect-test.md`,
approved before this attempt. For the finite-rank determinant use
M. Duits, *Determinantal point processes*, AppendixA Lemmas66 and69,
pp.51–52 of the [DPP2 author PDF](https://people.kth.se/~duits/static/media/DPP2.44e051d148b79af222fa.pdf),
as specialized and audited in L779. For elimination use J. Gallier,
*The Schur Complement and Symmetric Positive Semidefinite (and Definite)
Matrices*, 24 August2019, Section1 pp.1–2
([primary notes](https://www.cis.upenn.edu/~jean/schur-comp.pdf)).
The latter determinant factorization needs an invertible eliminated
block, not positivity. The symmetric positive-definite equivalence in
its Section2 is not applicable here and is not imported.

L777 gives A=U C Y^T on the original complex Hilbert space. All present
columns and residues are real. The cited finite-rank identity yields
det(I-A)=det(I-C S). Complete simple-pole residues are nonzero, so W is
invertible, C=J W^2, and the diagonal J commutes with W. Directly,

    W^-1 (I-C S) W=I-J W S W=M.                         (2)

This similarity justifies the proposed determinant transfer with its
signed pairing intact. It is not a congruence or a claim of symmetry.
In the negative-residue scalar block, B22=|d2|S22=-d2 S22. Symmetrizing
B does not change that diagonal. Hence

    D=D0=1-d2 S22.                                      (3)

The new work is an entrywise transfer from L779's complete saved data
to this actual quantity. Its full-operator trace error alone would not
bound the chosen coordinate entry of C S, so we instead use the saved
factor, node and complete-residue error bounds.

**Complete input bounds.** Hats below mean the exact decimal choices
in L779's independent-phase certificate, not sampled true values. Let
Hhat=H(bhat), where bhat uses all 512 certified positive Laurent modes.
L779 and L777's full infinite-tail error prove

    ||H(b)-Hhat|| <= delta_b <1.164e-12,
    ||Hhat|| <= h_b <10314.

The exact saved upper endpoints, rather than these rounded numbers,
are used in the rational certificate. At node2 the complete errors are

    |alpha2-alphahat2| <= e2
        =6.7762635780344027125465800054371356964111328125e-21,
    |d2-dhat2| <= e_d2 <2.8e-17,
    |alpha2|,|alphahat2| <= a=7/8,
    |dhat2|+e_d2 <0.000090002.

For orientation, alphahat2 is approximately -0.863137012840004864
and dhat2 approximately -0.0000900015058632706622. Only their complete
saved decimals/error enclosures are used. In particular e_d2 includes
the uncertain zero, F value/derivative and other root in the residue;
it is not merely an error in F. Both saved complete residue intervals
are checked to have the stated opposite signs.

The full finite-pairing enclosure implies

    -11119.388666759168086034 < Shat22
                            < -11119.388666759168086033,
    |Shat22| <11120,

where Shat22=v(alphahat2)^T Q3 Hhat v(alphahat2). This is the exact
finite polynomial pairing including all its rows; later Hhat rows are
zero. L779's saved finite entry encloses its finite arithmetic exactly.

**Actual pairing-entry error.** For real |x|,|y|<=a, the geometric
series and the finite-power difference identity give

    ||v(x)||^2=1/(1-x^2)<=64/15<9,
    |x^n-y^n|<=n a^(n-1)|x-y|  (n>=1).

The l2 norm is at most the l1 norm for these summable differences.
Summing n a^(n-1) gives (1-a)^-2=64. Thus
||v(x)-v(y)||<=64|x-y|; the n=0 term vanishes. All sums converge
absolutely, uniformly on the stated closed interval. This elementary
specialization supplies explicit constants rather than a new theorem.

Write v=v(alpha2), vhat=v(alphahat2). Splitting the full difference as

    S22-Shat22
      =v^T Q3 (H(b)-Hhat)v
       +(v-vhat)^T Q3 Hhat v
       +vhat^T Q3 Hhat(v-vhat)

and using ||Q3||=1 proves

    |S22-Shat22| <= E_S=9 delta_b+384 h_b e2 <1.06e-11.   (4)

This retains the one-sided projection and the actual b=p/F through its
complete coefficient and infinite-tail enclosure. No symmetry, pointwise
sign of b, norm<1 or desired minor sign is used.

Next split d2 S22-dhat2 Shat22 as
(d2-dhat2)Shat22+d2(S22-Shat22). Its modulus is at most

    E_D=e_d2 |Shat22|+(|dhat2|+e_d2)E_S <3.13e-13.        (5)

Combining the entire saved Shat22 interval and exact dhat2 gives a finite
interval for Dhat=1-dhat2 Shat22. Widening both ends by the full (5)
yields the outward exact-rational decimal enclosure

    -0.0007617242876228820175 <= D
                              <= -0.0007617242869983545388.

This proves (1). The upper endpoint is strictly below -1/1313, proving
the inverse bounds. Now (2) and L779's independently audited positive
det(I-A) make det(M)>0. Applying Gallier's invertible-block determinant
factorization gives det(M)=D T and hence T<0. This last sign is only a
consistency consequence; the adverse block (1) did not assume the full
determinant's sign. There is no reason to evaluate the reference-minus-
defect margin after both required first-stage conditions have failed.

**Certificate and scope.** Implementation:
`scripts/actual-fredholm/balanced_schur_442.py`. Full exact bounds,
selected complete input values, hashes, all checks, required/actual
thresholds and the empty failure list are saved in
`scripts/actual-fredholm/balanced-schur-certificate-442.json`.
Reproduce without overwriting evidence using

    python3 scripts/actual-fredholm/balanced_schur_442.py --output scripts/actual-fredholm/balanced-schur-replay-442.json

All new arithmetic uses exact Python integers/Fraction. The input hash
matches the file audited in step439; this identifies the input and is
not a new audit of it. No theta evaluation, contour count, Fourier
replay, parameter sweep, precision change or norm/determinant
recertification was performed. The inherited Decimal/mpdecimal contracts
and lack of independent executable attestation remain explicit. This
specialization establishes a new local obstruction to the proposed
certificate; no novelty beyond the inspected sources is claimed.

## Mathlib

Full matching coverage has not been checked. The cited Sylvester
finite-rank identity and general Schur factorization, together with
elementary geometric-series, Hilbert norm and exact-rational inequalities,
are the informal inputs. No matching Mathlib theorem, absence result or
formal verification is asserted.
