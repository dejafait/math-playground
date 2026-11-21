# Weighted common-profile attempt, step163

The supplied SPECIALIZE assessment is reused unchanged for its exact
target. This is one REPRODUCTION proof attempt, not a literature turn.
Main gap: L030-L032/C032a actual-Xi all-degree mixed positivity.
Intermediate purpose: decide a necessary symmetry condition for the
fixed exp(-P/4) form while keeping L910's all-complex-zero domain.

Read L909's complete proof/audit, L910's complete proof/audit, the
defining and ODE ranges of L906/L907, L908(1), and the recorded dt/t
stop/domain-audit continuation. Existing work is preserved. No use of
L908 step154, RH, simplicity, numeric zeros, or sibling notebooks.

Unfinished reasoning checkpoint: L910 bounds W on |Im z|<=1/4 and
q by 24*pi*exp(2|Re z|). Cauchy disks of radius delta=1/16 about
|Im z|<=1/8 fit strictly inside that strip. Their real coordinates
differ by at most delta, so the W envelope should give uniform
derivative envelopes through order four with a weakened positive
superexponential constant. This is the candidate way to pay the
complete derivative tails after multiplication by q.

Still to verify before claiming a result: exact-zero cancellation for
every shifted derivative primitive, endpoint signs and alpha-uniform
error, F's own Fourier shift/domain identity and positive form norm,
then a simultaneous distinct-real-pair bound. The finite-rectangle
identities may have constants depending on alpha; the final horizontal
tail estimates must not. A failed sufficient estimate alone would
leave symmetry unresolved. A full uniform vanishing form-norm error
and positive limiting norm would yield the required nonzero Gram entry.

No verdict or new lemma has been established at this checkpoint.

## Completion of this attempt

The subsequent full argument is canonical in
[L911](../lemmas/L911-weighted-common-profile-excludes-fixed-exponential-momentum-symmetry.md).
The narrower-strip derivative bounds and full q-weighted tails yield
the requested C/alpha form-norm error. F has positive form norm, and
the joint Gram estimate gives a nonzero entry for distinct sufficiently
large actual positive real zeros. This is an informative negative for
the fixed metric, classified REPRODUCTION; the proof awaits a separate
conceptual audit. It does not settle mixed positivity or other forms.

The new DAG row was checked against the canonical proof's actual
input uses. No pair symmetry or Xi positivity is assumed.
No mathematical script or numerical certificate was needed.
