# Moving-band root-count attempt1366 — working record

Approved target: the exact moving-band count in assessment1364, as
completed in review1365. This is a mathematical SPECIALIZE attempt.
Main gap remains L030-L032/C032a actual-Xi all-degree positivity.

Read the supplied overview/DAG/assessment, C019h's full proof and audit,
C019c's conventions, L018/L021 and C019g's normalization passage;
reused assessments1361/1362 and stops1345/1355/559. Existing local
changes are extensive and remain preserved. No cross-notebook input.

Partial reasoning, not yet a completed theorem: C019h provides fixed
positive a_-, a_+, r_-, r_+ and c_D with alpha between a_- d^(-1/4)
and a_+ d^(-1/4), r between r_- and r_+, and |D_q|>=c_D alpha.
Thus ell_q=epsilon_0 alpha and n_q>=epsilon_0^2 c_D a_-^3 d^(1/4).
The cited local Gaussian estimate would then give relative error
O(d^(-1/40)); C019h's complement supplies a separate vanishing error.

Remaining checks: verify local normalization and conjugation, retain
all terms of the continuous phase, then use the exact source derivative
S'=r^2 sin(2 alpha) (not its upper-span bound). For alpha small this
suggests d*(S(q_+)-S(q_-))>=r_-^2 a_- d^(1/4), where
q_-=q_e+d^(-1/2), q_+=q_e+2d^(-1/2). A bounded phase correction and
the ordered integer-level argument could pay the finite count losses.
Compare q_+ strictly with q_e+M sqrt(log(d)/d) using the same q_e(d),
and transfer through X=-T^2/(d q). These checks are still in progress.

Continue only with full normalized error <1/2, a positive growing
lower span, strict open root intervals and exact bulk separation.
This would recover omitted near-edge roots but leave the larger
far-end loss, every-degree hyperbolicity and global positivity open.

Completed1366: the full proof and citations are now canonical in
`lemmas/C019i-actual-jensen-moving-band-root-count.md`. The checks
above succeeded with a common existential onset; the result awaits
a separate conceptual audit. This draft preserves the intermediate
reasoning only and supplies no additional theorem or current routing.
