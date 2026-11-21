# Truncated Li counting-error attempt — step218

Approved target: prove the pointwise O(sqrt(n) log n) bound for the
K_n integral against d(N-M) on (sqrt(n),infinity), with multiplicities.
The supplied SPECIALIZE review216 matches the checkpoint action exactly;
reuse its HSW counting theorem and Folland Thm3.36. No new source gate.

Unfinished calculation: E=N-M admits |E(t)|<=C_E log t on t>=sqrt(2)
by HSW plus compact boundedness. With theta=2n arctan(1/(2t)),
theta'=-n/(t^2+1/4), |K'|<=2n/t^2, 0<=K<=min(4,n^2/t^2).
Finite integration by parts should yield K(U)E(U)-K(T)E(T)-int E K'.
For NBV, extend E by zero below T and constantly above U; extend K
continuously by a finite ramp below T and constantly above U. The
lower jump in E is excluded. Upper boundary vanishes for fixed n.
Expected bound: C_E[4 log T+2n(log T+1)/T]. Need complete the
extension, convergence and uniform-constant verification before claiming.

Direct local inputs intended: L018 and L978 (absolute model-tail
convergence); L977/L968 are conventions and downstream context only.
Smooth model matching and actual finite-head signs remain unresolved.

Completed: the exact finite identity, NBV extensions, convergence and
uniform constant are now proved in canonical L979. The bound is
C_E*(1+sqrt(2)+2/log 2)*sqrt(n)*log n, with C_E fixed by the counting
theorem and compact boundedness. No numerical or mathematical script
was required. This draft retains the initial unfinished reasoning;
the canonical lemma contains the full proof and qualifications.
