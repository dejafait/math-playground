# Finite Rice budget working record1661

19 November2026. In-progress mathematical attempt under the unchanged
SPECIALIZE assessment1659; source-notes1660 are reused. No new source
coverage or central sign mechanism is claimed.

Target: the exact three-edge A_d in assessment1659 at h=d/log(d),
c=-1/4 and right edge d+1/2. Main gap remains L030-L032/C032a;
paying this budget would only leave a finite signed comparison.
Continue with a full uniform upper bound at the requested threshold;
stop this budget only with a rigorous integrated contradictory lower
bound. Signed margin, x-range and C028b height transfer stay open.

Loaded C048k (including its audit), C048j's contract, C048a's principal
branch proof, L828 Section2 and L829's actual definitions. Reused the
primary source/duplicate comparisons1656/1660. No matching prior
degree-coupled bound found in the scoped Rice/Mellin records searched.

Unfinished mechanism: write F=E B_d and replace I by S only using
C048j's uniform relative error. On the top, sectorial Stirling applies
to s+1, p=s+1/2 and d+1-s, all of modulus at least h. Reflection
gives B_d=(-1)^d*pi*Gamma(d+1)/(sin(pi*s)*Gamma(s+1)*Gamma(d+1-s)).
The derivative of the log modulus of the resulting Stirling main term
appears bounded by -log(d)+4loglog(d)+O(1), uniformly in Re(s).
This must be proved, without differentiating an asymptotic remainder.

At the left corner, -s=conjugate(p), so the alternative exact identity
B_d=(-1)^(d+1)*Gamma(d+1)*Gamma(-s)/Gamma(d+1-s)
cancels the two gamma moduli exactly. C048k Section4/(11) and
C048j suggest log|F|=-(pi-1/2+o(1))*d/log(d)^2: the gamma quotient
adds h^2/(2d), whereas log|I(1/4+ih)|=-(pi+o(1))*h/log(h).
No completed all-edge conclusion is asserted at this checkpoint.

Right edge still needs a uniform proof, including t=0 where
d+1-s=1/2-it can stay bounded. The direct product B_d there is
bounded by d!/product_(j=0)^d(j+1/2); a polynomial bound plus a
uniform rapidly decaying E estimate may avoid compact gamma issues.
If completed, canonical proof will be C048l; no new mathematical
script or numerical certificate is currently needed.

Completion1661: the full analytic attempt is now recorded canonically
in C048l, including the uniform decreasing horizontal main term,
left-corner coefficient pi-1/2, whole right-edge product bound and
integration lengths. The requested budget is established by that
proof, pending a separate conceptual audit. The earlier notes above
are retained as the unfinished-work checkpoint, not a second proof.
No numerical script was needed. The next pass should audit this same
target using unchanged assessment1659; the signed and height gaps
remain unpaid.
