# Suzuki form audit working record1122

Research in progress under the unchanged SPECIALIZE assessment1121.
Target: the two exact form bounds in Suzuki Theorem4.2, not a full
positivity theorem or a new signed arithmetic mechanism.

Proposed route, not yet a completed audit: for positive x put
q(x)=integral_x^a phi(t)dt; for negative x put
q(x)=-integral_(-a)^x phi(t)dt; extend by zero outside [-a,a].
Keep its possible jump at zero, whose size is integral phi. Absolute
Fubini should give Phi(phi,z)=i integral q(x)exp(izx)dx without
mean-zero, parity or sign restrictions. Check q and each exponential
weight lie in L1 intersect L2, and convert Tao's negative-2pi Fourier
normalization. Expected identities are E_y=2pi integral
exp(-2yx)|q(x)|^2dx; expected constants C2=exp(2ca1) and C3=2T/pi.
The low-band estimate should follow from Cauchy--Schwarz on the support.

Read primary Suzuki v4 Theorem4.2 and the two displayed form passages;
checking PDF conjugation and normalization before concluding. Prior
screw source screen explicitly flagged the pointwise-to-form gap.
L739/L740 concern a different Suzuki parameter family and do not supply
these inequalities. No local mathematical input, new zero estimate,
cross-notebook theorem or mathematical script is needed.

Continue only after both inequalities hold with all quantifiers and
both frequency signs, or record a rigorous violating test; otherwise
retain the unresolved issue. All-window signs, low-block coupling and
the transfer to L030/L032/C032a remain open.

Completed: both target bounds pass. The complete proof and qualifications
are in [C618a](../../lemmas/C618a-suzuki-shifted-and-low-frequency-form-bounds.md).
The preliminary expectations above are now justified there, not an
independent certificate. The printed two-form passages were checked
in PDF text with HTML for conjugation; screenshot retrieval exposed
no viewable image through the available wrapper and is not evidence.
No contour deformation or pointwise-to-form inference is used in the
replacement proof. Remaining source-proof constants are only nominated
for separate review in assessment1122; PROGRESS.md holds current routing.
