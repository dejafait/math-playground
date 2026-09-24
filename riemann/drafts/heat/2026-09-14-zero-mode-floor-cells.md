# Zero-mode floor cells — checkpoint

L189 is complete; no interrupted proof was found. Planned finite reindexing:
K(u,r,v)=J(u,r) intersect [sqrt(uv-r),sqrt(u(v+1)-r)), with gcd(m,u)=1 retained.
The strict upper boundary is essential, including at v=4N² where the closed
support endpoint can survive. Define T(v)=sum_(u,r) P(u)/u sum_K H_m(r).
Then Z=sum_v Q(v)T(v)=sum_(c,d in I)q(c/N)q(d/N)T(cd).
Each floor cell has bounded length, but summing all cells must retain the
original O(h) m count. Cancellation is unproved.

Resume: prove exact endpoint formula and signed-profile criterion, add exact
rational regression checks, then update DAG/history/progress and validate.

Completed: L190 proves the exact partition and profile identity. The rational
regression script passed; cancellation is still explicitly unproved.
