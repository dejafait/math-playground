# L091 — L090's fixed witness fails remaining nonzero-old-block modes

## Hypotheses

Use n=1024,w=68, L021's original pair prescription, L053's positive
singleton rho, and matrices divided by rho. Freeze exactly L073's
included-anchor five/six/seven PSD base and L075's entire dictionary,
including the original seven-column RREF/completion. Import all ancestral
PSD, uniqueness, whole-kernel and coherent-normalization qualifications
in foundations/04,09,10,12; no recursive ancestor audit is claimed.

Use L076's original affine columns at exactly L086's parameters, with
t78=L083's stationary s and p8=16792471/1181138102168120460>0.
Freeze all 45 L090 moments, not L086's or L088's different moments.
They are the complete rational vectors `witness/z` and
`witness/raw_moments` in
`scripts/finite-support/fixed-column-zero-old-block-results.json`;
L090's deterministic pivot recipe specifies this same witness.
Keep the 85 original domain rows, 90 kernel equations, 500 types/3000
presentations, 36 forced entries, full anchor and original pairs.

Write i=9a+b, 0<=a,b<=8. Let I={9a+b:0<=a<=6,0<=b<=3} be the
28 equality indices. Let Z be the entrywise zero-old-block indices
specified and audited in L090, including empty blocks. Only evaluate
J={0,...,80} minus (I union Z); no variable is optimized or retuned.

## Conclusion

At this complete assignment, exactly 14 of the 30 J-mode remainders
are negative, 16 positive and none zero. The failing indices are

    6,15,23,25,31,32,34,42,49,50,52,60,67,68.

The minimum scaled remainder occurs at i=31, mode (3,4), and is in

    [-260419060753567,-260419060753566) / 10^6,

strictly below the required bound zero. The full exact value is N/Q:

```text
N=-92224108459593073033260204480918415815376972912372608967267856501410960393783333481656646279742232645259615540700528491361767617985482502007691256261296447709446507644496432190623462320094608553920311984698416973133603930178021240380945792432117910939932783674919913647591995417269804193953725463917095069368108847521948462713708500194342380867373078803505794614925014593294574957520179839623231427419308042012046519057477699354377697110033106822752852097862760602320811382568372205497258076494126681890414757078269382286087762324459422093056535583750000881815258982967131031412192586524685251413151039227671845461870662781646415616879364149530313295713669710281534215677892968935180182157149501996823341834654116260370349975128428272599479061647922046410769736998951537171005794874347610990040319278315192626168633873968312626251511633201146601863774406958894702409556716729963087731919721027127276227637167434107381502718397813064401031565432720723540995719155319875354036205096931656059592662282549251528892777503597320702574949074841159555154615609660181080623903606232758417486766780785333139468872744737928421727562126808478461633288789613678553139687735532889672392628722982799577798642300789496884067187204932089972355147540474878138169028860856407932141778603689118442674354297429611846693384892882501076404815667016750200140320655105498322473346241232931998924515718080125370236956356093319301066326123554300329826134942913893569212310276570883287507560834119681307146663505099205560908371857361354496256576525662585234700349232276634336024263002744447122900284950435385472216381107525431632948166992900538205525852954217668560523134721404332337264773447166755123858109626281425420538424349357421702114199860216306547302609190894381629163889642325781859864045170406144014175063066991593368926836103751767087216964408161043999849809037024853748912272811657836640792295539778963948234862484740856504355051325538565195583950810343220233632187928923267024477967536272538659055012760236663173849280055737324841831533616839975874644303398466998565545468071871165374131342499852141028973435908082277384912689546635531013099175975777176296547864527553357595930771030527351469378100413858020496775031767436626084055731470285847902288978427439162364855928716148761959859714933567314702539704697790906530188407585936146371082819002826700855516370162110008606783823592751187245801595656702730572803834844984535856526855505993059163923256391870131852021663173398579009531379144051143712736061475901506859580273938730652535464294922425743384503232867702618486256751026309524621367467195793756698606923632109810767165814208748072114203032351863964445211466478646987738384656999231903180996395337118573372240506678903173939044028563838806418428920646042575930097509318703164214594328484312963106751861044709995600893034037144195378756678739004253209450011004872010214721341671390187201171940456251861424021800129054600333880379994577752343221001403875010108713542723217709007491673598814845135101962579188685453879711805722817131330969232896923715820776366122964305959657917769025151429523869081301238907977093235952853595194807236030260715285760846025078545381266342242434630588475348611196377159975675131068186091615220500382495314742050480267197868052220989045836689799899606170979266913435921260417334411256150299411541110514155032465310181641818896259762195126661241860479568862805445703695444050526931371001788728494138897019054568404609516660474647000220977777974659340445487684681923779031666335108583698811608996154827283183542005151328991274131697707548689002297682258968118379003417640510403558909071394686402720688159967472625244913698487308361942041372415483437932398977506141716444824240936034052705082741856099272229995459085251890885631946787592846843803596912711396645200903153798176698840676106374159385998165198626920878838256458005464591069301959456146775831204174663784636000534541507950562877182972686474686864118262287133484468535469193104888943179608138098719936313791305518962042152450917069671206127580858007240839775611763669415726832301227269936800629077770883275488402049588606901067224202706940811858285986252789525869833321072485108122059044146898889945157227938072280112335606941938379887932579880015160364580099496051155449510043737327485022715521113378189183002375111137939669335567053774339947882748301438464518361975634907594722453699
Q=354137320796439430220027782788689060001917338026202311343219943222130420351509495558267609057867434001983587871346500180304543386546895034940465064686732949800359417804136039409277472960660148885346136298686541990012824884262827753692088400868897967449917931196411451330484155351452397332924698458532218536424966760152322938263450464498373261041077787794877853150680573784972945427829550726307201998446838467320635672211488412786738097102191255337813799869392900924517485236008536784235560155093890514095687052953966154117789589397745052530432473513813850103104074993215247836989303101940131818300204717981792218766658156141344783340179797274092755284780718864434400189066255426391220110382420371155152652636589403286025755903133545917715227321943663745415927324081099612634836429051489964261906725247285159234492230590349652469101338020148562852808041722022954713499919004435645382360770683077861837607140366259998185980159751624640383499990969209285379396236513583438635393027339363961328520229249887334714787571721350411616600346720915518199986600687884378414340278822772424853249021326402960442274570505832315670587434245690003948447388418914675636495697575355580951124343570232099488632212415392422808753599908076838182709892783663465502036292124627568493837730866812807111318714746949095164761041324438504490067749168124183622596290267897175795769693990726297084740209989681484588329123611007700100278954446672234676006976253190155378605647317627985917804241155397698232461668177199574914533438049671388438699011378897276379046895406584285651201926919047413268227961169008658928787370626149413439213969217668093486434741118335520333820631373870781859247892366910093787086800519579223566314472723183921115813909130266531034384285922347572235150185738194184175346205002360549931041430687448845362045265821486359930412271705865601084137390629693072161344490403003346020150470074298590329897850047107625452749452069546176706893563139486252404904791680882140047788440770621035293039885721026609904513214853348273434407083894687066834223851202333259986918134440187695308749461085248817368952409352685346234136956658527340572635868222769942920916540325909130390411597266001661087909285522912489677535870780784700817770029082204702603786129590615435682044733734290453303202395609130886562033593399777582638327084044385217020863176460041471578097046315457360027720703114060661916665046346949700179943110641265542893319909300866677761736673382283236040753784354998744149860351978278273920890424983591410547817532489457922872871484269826693569858003800215367492517885511440446821453989881033538763450432713514320676897519289882885282278470894582671039373203644445671302891260494094744202525740208702034106543932265452783444217776406756885830257440777664430564872063077828701566826590821122623757925546344352553783074277127635304624683025389518574286429181664442276550399555898543080727549067304289628386450703567589648735725483182298793535830584662980053540597179583266663446400602702035351570146973098858918177809559839627333620661224535388725906542876694009391334779624959854538438274833120551264657054787670449593223328343416868732634161575213017020776584752516130611615710066513080910366781029407617902948024872046225135958135392553391220587802477096225454004357732573763136460170158275079261094192477060890606056499754507377861290213313542435799908229640273284905354873991599625577395615802071753180849804938310915998886544094685992743805253951340345757408762077962065789578693436320199078772732408520665337594211013541504999631244041374781005037760328705071914185436766729596914088154002157962529935680772894222226982030113412239678629743201536917543548732246163424753342030181912196992126952909616487890967725715905305157129483533871154747236809488572302771676180294436946843888037490588271084259918494251637836673509605250109577613272195406076287585174728862966000094873477746821814221306320865799963791387826266770481393987494551653933574519226805115630321240547514115863224637890024170500010461179546293043659315750380468456747042344468155861738645231357825129576197666104330328649927628831178627762919828565718181766697042291380409617997678491528239184333257941051825691591655080371383343006994299762742423349739478797835645829349713331333971629229147529791170275777994617392142350612409496337560745173082003440417093129789281894359664743259802031250
```

All 28 original/raw equalities remain zero. All 43 retained Z-mode
slacks remain nonnegative, with ten positive and 33 zero; all 45 moments
remain nonnegative, with 35 positive and ten zero. The 85 domain rows
and all original/weighted kernel equations still hold.

Thus this fixed complete assignment fails the included-anchor PSD test.
This does not exclude a different 45-moment completion at the same
columns, other plane points, columns, bases or pairs. Scalar upper rows,
other anchors, global consistency, representing measures and RS
realization remain unresolved. L090's necessary-subsystem pass and all
older fixed-assignment rejections remain valid. The arbitrary-center
67/68-agreement gap and bracket 955–957 are unchanged. This is local
RESEARCH / REPRODUCTION progress using known methods, not a new general
theorem or a claim of progress beyond the sources checked. The separate
conditional critical proof review below retains this finite verdict.

## Proof

**Precise known inputs and specialization.** Reuse the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-zero-old-block-witness-remaining-mode-residuals.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Its two ground sets here have sizes 68,956, with layers
0,5,6,7,8. Principal restriction and L078's coherent positive congruence
retain both rectangular directions, all modes and positive multiplicities.
No actual-label restriction is transported or averaged; the suspect
complement prefactor (61) is unused.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2 Corollary 2.2, Theorem 2.6 (including both singular proof
directions), Lemma 2.7. Finite real symmetric blocks are covered;
finite-dimensional ranges are closed. Retain old PSD and the entire
range condition, including singular nonzero blocks. A checked solution
B*x=c computes c^T*x independently of which solution is used: the
difference of two solutions is in ker(B), orthogonal to c in range(B).
This does not identify an arbitrary quotient inverse with a Euclidean
Moore–Penrose inverse.

The ordinary union-moment context is imported from Sven C. Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*, IEEE TIT
65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and indicator proof p.2,
Section 1.2 p.3. Its constant-weight parameters are n=1024,d=10,w=68.
Neither a representing measure nor RS realization is inferred. These
known results need no reproof; none supplies the fixed residual values.

**Original rows and raw identity.** Binomial coefficients outside their
ordinary range are zero. Use exactly the source convention

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t) C(h,t) C(n-2a,h-a) C(n-a-h,l-h) C(n-a-h,m-h).

Let S_l=C(68,l)C(956,l). In mode i=9a+b the old layers are
l in {5,6,7} with l>=max(a,b). For the fixed raw dictionary Y define

    T_lm=sum_(j,k=0)^min(l,m) beta(68,l,m,a,j)beta(956,l,m,b,k)Y_lm(j,k)
         -1_(i=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm) on the old layers, c_i=(T_l8).

The constructor rebuilds these entries from original pairs, the old
completion and the full affine eight-column dictionary, checking both
rectangular directions. It independently reconstructs every full-key
presentation, all forced/free entries and the weighted kernel equations.
All 306 old principal minors are nonnegative. For every mode it checks
B_i*x_i=c_i in every coordinate, including empty and singular cases;
it also checks all five affine coefficients of the range equations.
A fresh invertible principal minor gives one solution by Cramer's rule,
with zeros outside that minor; direct substitution checks the full
system. Its energy equals that of the saved affine inverse action.
No range conclusion is inferred from rank labels alone.

Index the 45 free coordinates by (r,q) in lexicographic order,
0<=r,q<=8,r+q>=8. Define

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q),
    Y_88(8-r,8-q)=p8*z_rq/V_rq,
    D_i=C(68-2a,8-a)C(956-2b,8-b), M_i=p8*D_i>0.

Let F_i be the forced part of the full raw new diagonal beta sum,
H_i=1_(i=0)*p8^2*S_8^2, and K_i=c_i^T*x_i. Reconstruct

    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    b_i=(F_i-H_i-K_i)/M_i.

For this fixed z, direct rational substitution gives

    R_i=F_i-H_i-K_i
        +sum_(rq) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)*p8*z_rq/V_rq
       =M_i*(b_i-A_i*z).

All scales are strictly positive, so original and raw signs agree.
The full anchor and inverse costs are retained. Nonzero old blocks
are not treated as invertible merely because they are nonzero.

**Exact partition and substitution.** Check every old matrix entry to
select Z, reproducing all 81 L090 membership decisions and all 43 whole
cross zeros. One obtains |I|=28, |Z|=43, |I intersect Z|=20 and

    J={4,5,6,7,14,15,16,23,24,25,31,32,33,34,40,41,42,43,
       49,50,51,52,58,59,60,61,67,68,69,70}.

The selected equality/zero-block union has 51 elements and its
30-element complement is exactly J. Substitute the unchanged L090
z and raw moments in every original/raw row. The complete output
`scripts/finite-support/zero-old-block-witness-remaining-modes-results.json`
stores all 81 rows, every original/raw residual and all failing fractions.
Its `/rows/31/scaled_slack` is precisely N/Q above; integer cross
multiplication proves the stated strict interval. Every retained
residual equals the corresponding complete L090 certificate value.
This proves the exact sign counts without rounding or an optimizer.

For an explicit failure certificate let d_i be the complete transported
new diagonal F_i-H_i plus the free raw beta sum, and form

    C_i=[[B_i,c_i],[c_i^T,d_i]], v_i=(-x_i,1).

Using the checked B_i*x_i=c_i gives

    v_i^T*C_i*v_i=d_i-c_i^T*x_i=R_i.

At i=31 this is M_31*N/Q<0. The full exact 4-by-4 matrix, vector and
negative value are stored under `/offending_block` in the same file.
Thus one explicit vector violates PSD. The independent verifier also
reconstructs its diagonal from all 81 raw orbit terms, including forced
entries, and checks the saved vector against the full block. This
negative quadratic form does not require a numerical eigenvalue.

**Complete verification and limits.** Reproduction commands, with no
constructor, optimizer, retuning, scan or new separator, are

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/zero_old_block_witness_remaining_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_zero_old_block_witness_remaining_modes.py

The finite substitution has 1214 passing checks. The independent
verifier has 5044 passing checks and no failures, saved in
`scripts/finite-support/zero-old-block-witness-remaining-modes-verification.json`.
Five additional exact manuscript checks pass in
`scripts/finite-support/zero-old-block-witness-remaining-modes-manuscript-check.json`,
including the complete rational and strict interval. The independent verifier
uses the Johnson eigen-coefficient expression

    e(n,a,r)=sum_(h=0)^r (-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h),

checks beta(n,8,8,a,8-r)=C(n-2a,8-a)*e(n,a,r) for every used
coefficient, and independently computes bounds with the saved original
inverse action and all range residuals. Every original/raw remainder
agrees with the first calculation. Complete relevant step-318/320/322/324/
326/328 arrays are consumed with their actual schemas; shared columns,
keys, kernel rows, base/cross, forced terms, anchor, coefficient rows,
bounds and norms agree. Old witness residuals remain distinct regression
evidence; no L087/L089 verdict is attributed to L090.

An added prior-array wrapper initially stopped before its residual
substitution because step-318 reconstruction rows name their scale
`positive_raw_normalization`, rather than `raw_norm`. The record is
`scripts/finite-support/zero-old-block-witness-remaining-modes-verifier-schema-failure.json`.
Explicitly handling the recorded schema names changes no coefficient
or witness. The completed verifier above passes the full comparisons.
This is not a failed mathematical comparison or an optimizer restart.
A narrow early verifier had already passed 546 substitution checks;
only the completed 5044-check certificate is used here.

The known methods and imported ancestral qualifications limit the
verdict to this exact assignment. No full-column exclusion, scalar
upper-row pass, other-anchor PSD, global moment extension, packing,
RS list or threshold improvement follows. The historical full-row
cap and conic stops are preserved. The first arithmetic checks do not
recursively certify all ancestral hypotheses; the separate audit below
retains exactly the stated conditional scope.

**Separate conditional critical audit, 2026-10-18 (step 332).** The
pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-18-zero-old-block-remaining-modes-critical-audit.md`.
The known inputs cited above apply with the same hypotheses; no new
general theorem or recursive ancestor audit is used. The independent
source reconstruction rebuilds the original pairs/rho, seven-column
RREF/completion, eight-column family, all 85 domain values, all 90 affine
weighted kernel equations, all 500 types/3000 actual-support presentations,
and the 36 forced/45 free partition. All 220 unequal-layer subset
transitions in both directions are reconstructed with independently
orthogonalized bases. Positive multiplicities and complete layer dimensions
are checked. Its old L086 remainders are regression controls only.

Here is the normalization connecting the negative certificate to the
matrix, rather than merely to a scalar row. For each ground set n and
layer l, let h_(n,l,a) be the monic orthogonal polynomial of degree a
under weights C(8,i)C(n-8,l-i), and let nu_(n,l,a)>0 be its squared norm.
The complete transition matrices have entries

    T_(n,l,m,k)(i,j)=sum_h C(i,h)C(8-i,j-h)
                           C(l-i,k-h)C(n-8-l+i,m-j-k+h).

Their checked actions are T*h_(n,m,a)=g_(n,l,m,a,k)*h_(n,l,a);
degrees absent from the target layer have zero action. For every nonzero
beta coefficient the ratio

    sigma_(n,l,m,a)=nu_(n,l,a)*g_(n,l,m,a,k)/beta(n,l,m,a,k)

is positive and independent of k; zero beta has zero action. The checks
retain sigma_(l,m)*sigma_(8,8)=sigma_(l,8)*sigma_(m,8), separately for
both ground sets, and sigma_(n,8,8,a)=nu_(n,8,a)/C(n-2a,8-a).
With N_i=nu_(68,8,a)*nu_(956,8,b), define

    s_l=sigma_(68,l,8,a)*sigma_(956,l,8,b)/(N_i/D_i), s_8=1.

All these scales are positive. Direct weighted entries, including both
cross directions and the complete anchor subtraction, satisfy

    W_i=(N_i/D_i)*diag(s_l,1)*C_i*diag(s_l,1).

The audit recomputes all 81 new diagonals from all 81 actual raw orbit
values each, using the independent beta and direct subset-action
coefficients. It checks the new diagonal relation as well as every
old/cross entry. Consequently the negative vector for C_31 supplies a
negative vector diag(s_l,1)^(-1)*v_31 for W_31. The positive multiplicity
and nonzero orthogonal basis place this block inside the prescribed
matrix. This is a finite specialization of the cited block theorem;
no arbitrary-label averaging or quotient pseudoinverse assertion is used.

For every old block the audit checks all principal minors and obtains
a fresh inverse action by Cramer's rule on a nonsingular principal minor,
followed by substitution in every old row. Empty and singular nonzero
blocks remain included. The full affine range residuals also vanish.
The fresh energies agree with the checked weighted elimination energies.
Every current original/raw/weighted remainder agrees; each of the 30
complementary signs, all 28 equalities, all 43 zero-block controls and
all 45 moment signs is retained. Complete relevant step-318/320/322/324/
326/328/330 arrays are compared using their actual schemas, including
the full step-328 witness. The older L088 residuals are independently
recomputed at L088's different moments as regression evidence only.

Every entry of the saved 4-by-4 C_31, its four-coordinate vector and its
quadratic value agrees with the fresh construction. Every digit of the
reduced manuscript N/Q, both complete index lists and the strict interval
is checked. Thus the negative quadratic form proves precisely the fixed
assignment's rejection, without any optimization or inference from a
numerical eigenvalue. The earlier scale-name exception is preserved and
explicitly checked; it changed no mathematical input.

Reproduce the separate audit with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_zero_old_block_remaining_modes.py

The source reconstruction passes 7993 checks, the independent original/raw
verifier passes 5044, and the additional critical audit passes 6681, all
with no failures. Full evidence is in
`scripts/finite-support/zero-old-block-remaining-modes-critical-source.json`,
`scripts/finite-support/zero-old-block-remaining-modes-critical-verification.json`
and `scripts/finite-support/zero-old-block-remaining-modes-critical-audit.json`.
The latter contains all current rows, complete raw/weighted diagonal sums,
the offending block/vector, and full manuscript rational.

An initial audit passed its mathematical comparisons but failed its
manuscript-index check: the parser selected the introductory symbolic
definition of J instead of its indented explicit list. Its complete output
and script are preserved as
`scripts/finite-support/zero-old-block-remaining-modes-critical-audit-initial.json`
and `scripts/finite-support/critical_audit_zero_old_block_remaining_modes_initial.py`.
Anchoring the parser to the explicit list repairs this documentation check.
The completed run used `--reuse-reconstruction` to reuse the unchanged
fresh source/verifier certificates and repeat the additional checks.
No mathematical discrepancy was found and no moment, column or mode
was changed. Ancestral PSD, uniqueness, whole-kernel and normalization
qualifications remain conditional; no other completion or RS boundary
claim is upgraded by this audit. Direct mathematical inputs are unchanged.

## Mathlib

Full matching fixed-witness residual/rejection result: not checked.
Supporting singular-Schur, invariant unequal-layer and rational arithmetic
coverage: not checked here. Unknown availability is not absence.
