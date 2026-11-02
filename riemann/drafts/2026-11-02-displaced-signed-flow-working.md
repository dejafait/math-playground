# Signed angular energy along the displacement homotopy

Gate reused unchanged: `literature/2026-11-02-displaced-signed-angular-sampling.md`
(EXPLORE). This is one analytic attempt on its exact TARGET, after
L666's inconclusive finite test. The main gap is actual-Xi positivity
and unbounded-height signs. The intermediate goal remains the uniform
H-versus-D bound; L658 supplies its possible paid-arc use. General
support, realization and signs remain independent.

Keep L666's exact family, unit residues, n=12q+3, and all moments.
For a proposed displacement vector epsilon, use
a_m(s)=x+i*(H_0*(m+1/2)+s*epsilon_m), 0<=s<=1; the anchor stays x.
No exponential surrogate or quadrature-weight positivity assumption
is made. The proposed test is a relative signed-energy estimate along
this path, not subtraction of an inherited-anchor error.

## Partial reasoning saved before closing the estimate

Write c_s=R^(-1) sum_a W_a(s), E_s=mean |c_s|^2, and D_s for
the actual diagonal. Differentiating the complete rational product gives

    V_a(s,u)=d_s log W_a(s,u)
      =-i*epsilon_a sum_(0<=j<n)
           [1/(a_m(s)-t_j*u)+t_j/(U*u-t_j*a_m(s))].

This denotes W'_a/W_a; no global logarithm is required. W_a never
vanishes on the angular circle for these real s. For the anchor V_x=0.
Hence c'_s=R^(-1) sum_a V_a W_a. The exact signed derivative is

    (log(E_s/D_s))'
      =2 Re mean(c'_s conjugate(c_s))/E_s-D'_s/D_s.

The first term retains every cross term. L666 gives E_s>0. Fixed-n
compact pole clearance permits differentiation under the circle mean.

For every path, |Im a|<9/20, |a|<273/200, and U-|a|^2>201/1600.
Thus |V_a|<=6n*27/(80n)=81/40. The logarithmic derivative of
the diagonal weight has magnitude at most 162/(67n). Consequently

    |D'_s| <= (81/20+162/(67n))*D_s.

This costs only an absolute factor over the whole path. It is not a
bound for E'_s/E_s, and no sign is assigned to any mixed term.

The remaining test is whether the signed numerator permits an
integrated logarithmic descent within the linear budget left by the
baseline and L661. Exact constants and the attempted closure will be
recorded before deciding whether this mechanism can continue. No
uniform response bound or countersequence is claimed at this checkpoint.

## Completed bounded attempt

The complete differentiation, diagonal constants, baseline L2
specialization, exact signed logarithmic loss and unresolved rate
comparison are canonical in L666 Section 6. This working checkpoint
is retained as unfinished reasoning history, not a second proof.

The diagonal varies by at most exp(17/4), but no estimate for the
signed logarithmic loss was obtained. The available absolute
Cauchy--Schwarz fallback is vacuous at the required scale and is not
a new obstruction to the actual response. Outcome: EXPLORATION.
This is the second unproductive attempt on scalar sampling; park it
pending materially new input rather than extending numerical screens
or the same norm inequalities. The full-spatial fixed-angle target is
nominated separately with REVIEW_REQUIRED. No RH candidate exists.
