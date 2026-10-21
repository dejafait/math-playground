# L087 — L086's complete sign/equality witness fails the remaining modes

## Hypotheses

Keep n=1024,w=68, L021's original pairs, L053's positive singleton
rho and L075's entire immutable dictionary. All matrices are divided
by rho. Retain L073's included-anchor five/six/seven base and the
original seven-column RREF/completion. Use L076's original four-parameter
column family, all 85 original domain rows, all 90 weighted kernel
equations and p8=16792471/1181138102168120460>0. Ancestral PSD,
uniqueness, whole-kernel exhaustion and source-normalization qualifications
remain imported; this is not their recursive critical audit.

Fix the **entire** rational witness of L086, not just its column
parameters. In its canonical `witness/original` array in
`scripts/finite-support/affine-sign-phase-one-results.json`, write

    w=(1,u1,u2,u3,z_0,...,z_44),
    t=(u1,u2,u3,s),

where s is L083's exact stationary t78. All 45 moments are fixed to
these z values. Their lexicographic indices are (r,q), 0<=r,q<=8,
r+q>=8, and

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

Preserve the other 36 eight/eight entries, the anchor, original pairs,
Boolean repetitions, forbidden distinct half-distances 1,...,4, all
500 full unordered types and all 3000 presentations. Retain all 81
included-anchor modes, including every singular/empty old block and
both rectangular directions. No scalar upper row, other-anchor
condition, actual-label restriction or global extension is added.

## Conclusion

At this unchanged complete witness, 19 of the 53 unselected original
mode inequalities fail strictly and 34 pass strictly. The 28 selected
mode slacks remain exactly zero. The negative original indices 9a+b are

    4,6,8,14,16,23,24,32,33,41,50,58,60,64,67,68,73,75,77.

In particular mode (a,b)=(0,8), index 8, has scaled slack sigma satisfying

    -6896215747443/10^12 <= sigma < -6896215747442/10^12 < 0.

Its old block is empty and it has no anchor correction. Its raw Schur
remainder is exactly

    (46806225362314/445376358283605)*sigma < 0.

The complete full-anchor original/raw residuals agree in all 81 modes.
Thus the included-anchor matrix specified by **both** L086's columns
and its 45 free moments is not PSD. This does not exclude different
choices of those 45 moments at the same column parameters, or another
point of the original zero plane. L086's sign/equality subsystem result
remains valid. No uniform upper bound, global feasibility verdict,
RS list or improvement of the 955–957 bracket follows.

This is a local RESEARCH / REPRODUCTION calculation using assessed
known tools, without a source-level novelty claim. The separate critical
proof review below retains this finite rejection with the same ancestral
qualifications.

## Proof

**Precise imported results and specialization.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-18-affine-sign-witness-remaining-modes.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Ground-set sizes 68,956 and layer restriction 0,5,6,7,8
are within the unequal-layer decomposition. L078's coherent positive
normalization and both rectangular directions are retained. All 81
modes have positive source multiplicities; a negative scalar in a
new-only mode therefore contradicts PSD. This algebra needs no code or
representing measure. The suspect complement prefactor (61) is not used.

For the other, possibly singular, old blocks import Takashi Sano,
*Moore-Penrose inverse, generalized Schur complement and inertia*,
version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. The retained real
symmetric PSD base and cross-kernel compatibility permit the scalar
Schur criterion, including empty blocks. No Euclidean quotient
pseudoinverse, Slater hypothesis or attainment theorem is used.

For ordinary equal-union moments retain Sven C. Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its complete indicator proof
p.2, Section 1.2 p.3. Its proof gives the constant-weight conclusion,
despite the displayed final notation. The fixed assignment here is
already invariant under permutations fixing the anchor; no extra
actual-label constraint is averaged. Foundations/04,09,10,12 preserve
these qualifications. No general theorem is reproved. The sources do
not evaluate this rational witness, so direct substitution is needed.

**Original system and exact point substitution.** Write C(n,k) for the
binomial coefficient, zero outside 0<=k<=n, and S_l=C(68,l)C(956,l).
Use exactly the original coefficient

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

For i=9a+b, 0<=a,b<=8, the old layers are l in {5,6,7} with
l>=max(a,b). L082/L083 specify the source matrix B_i, affine cross
vector c_i(t), forced contribution F_i(t) and anchor term

    D_i=C(68-2a,8-a)C(956-2b,8-b)>0,
    H_i=1_(a=b=0)*p8*S8.

Solve a largest nonsingular principal subsystem of B_i*x_i=c_i(t),
setting unused coordinates zero, and verify every original row. For
an empty old block both vectors and the cost are empty/zero. Define

    b_i(t)=F_i(t)-H_i-c_i(t)^T*x_i/(p8*D_i),
    A_(i,rq)=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D_i*V_rq),
    sigma_i=b_i(t)-(A*z)_i.

The original PSD requirement is sigma_i>=0. In full unnormalized raw
coordinates the same remainder is

    R_i=sum_(forced j,k) beta(68,8,8,a,j)beta(956,8,8,b,k)Y_88(j,k;t)
       +sum_(free r,q) beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)Y_88(8-r,8-q)
       -1_(a=b=0)*p8^2*S8^2-c_i(t)^T*x_i
       =p8*D_i*sigma_i.

Every scale p8*D_i is positive. The last equality is the previously
assessed coordinate-conversion contract, checked directly here in every
mode. The constant mode retains the full positive anchor subtraction;
the empty modes require no old inverse. All 36 three-old-layer, 13
two-old-layer, 15 one-old-layer and 17 new-only cases are included.

The exact original witness and raw moments are consumed in full and
compared coordinatewise with the complete step-310 audit and original
verification. Reconstruct the 85-factor family from the original RREF
with nonpivots 56,63,69,78. All 85 domain inequalities and 45 signs hold
at the same point. The entire 150-coordinate affine column retains all
90 original equations and all 90 weighted kernel equations coefficientwise.
Reconstruct every full type with atoms

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

All six bit-permuted presentations agree with the unchanged dictionary,
including reanchorings outside the selected layers, Boolean and forbidden
cases. This leaves exactly 36 forced entries and 45 distinct free keys.
Original seven-column/completion uniqueness is an imported contract,
not a conclusion of these comparison checks.

Rebuild all source beta entries from these complete keys. Compare every
base, cross, forced, anchor and free-row coefficient with the reviewed
family-mode data, consuming the full arrays. Check every coefficient of
each affine inverse-action residual. A fresh largest-principal solve at
the fixed point checks every row again, including singular/empty ranges;
its cost equals the saved affine inverse cost. All 306 old principal
minors are nonnegative. The reconstructed bound agrees with the full
saved quadratic bound in every mode. This verifies the inherited
coordinate contracts, without upgrading the ancestry's review status.

The selected set I={9a+b:0<=a<=6,0<=b<=3} has 28 members; its complement
has exactly 53 members, with no missing or duplicated row. Direct
rational substitution gives sigma_i=R_i=0 on I. The complement has the
19 negative indices stated above, 34 positive slacks and no zero slack.
All 81 exact identities R_i=p8*D_i*sigma_i hold. No sign tolerance,
rounding, optimizer status or aggregate separator is used.

**One load-bearing negative value.** In mode (0,8) there is no old layer
and no anchor term. Here D_8=C(68,8), and exact arithmetic gives

    p8*D_8=46806225362314/445376358283605>0.

Thus its negative sigma already proves the fixed matrix is not PSD,
independently of a choice of inverse on any singular old block.
The complete reduced rational sigma=N/Q is recorded below, with N<0
and Q>0; the raw value is its stated positive multiple. All decimal
digits are exact. The strict displayed interval is verified by integer
cross multiplication. The canonical machine-readable copies are
`rows/8/scaled_slack` and `rows/8/raw_Schur_remainder` in the results
certificate below.

```text
N=-549996394888113552645305874428847780317302448191854558558271801808080394297467593404101379201560729964244897585205981229358521576651253388546353585186377753995835196425803700161272243567409645341462570179294541859436708628929282907629094141772963314427624362941119187569144416549212125004829276581099492754390287695467784998988293618609227938198975135699504296340546098640031976723794109932376226875309251608086707780598857798629746941776929098624925939305473003949340188227723324143349128629147204509823919216453573814345289979374004741345663461303553864476445162734624327467408292448919058384332069113733076586312164079406043567852857920744115792400967047921677413447198772081902940381814880649405676496760315412380884204165283826886116084093730244785896239466528258726003510418093109267082697639979806430700240342198815241845929300174769202447462920605234604774075946342560585689033724103075788833095561551070537736986026177661159211438952155400187279547710972570633544512562700338959865428931193055629517313992302788933666517967849096089506286363381192125864509930441461263665294755666987067218541206167174241637856254024043820008547453269960145673280089018812026953268968197918912440254079990419639533283670315616918923926355474984473852956450131022672530251709730466796742680846708170264436004665578256951640878556930730788190660987099600607590950924789300017515302029711746484434823167565588829042927720667122871491476639824312692710976047100440011665026979345237409798063396914000711297831835134341389447788318912433666086335433548188150866105325367403963121904342858147877073991117270117457241849520263856866822529315276012710428926240360314145244110019946103125161735692698699984550183159283704743413172011046038439287870255931612785676424013181348662424069510340058987069498602363674382383756344244254440518166402989347093165488233210196971158578020009544677271348620895024001748785904914968916254098434769570215535579473333208057747871293353894636270670597451489018320528890329365487631233431368504721482722105698747511919574340180900302646245502985218192806730848218517885760816553574471196589924375532184140619065409410674725707553925443430316543503040476001395488223454686633057673236283105730704911445831755068335053370196106487887334056840197936726451158335749890711832187234010536456003213971823560050671985267133863346914455028270185759899514029099689607948318079922970585313259465797224027761067615950398982363907423331772705208511209891990931674575356305023350178711283407370804681457348657454470667695034522032382651603518151936473963547075260425784148466417842320774865727815792243003110361012250442764853619838046324232672279566849656859815267009726233124050269489300027001911292306313894450546713119189148043647759094802594409180179640053665448166793813231155631817284012437505226410293139982837410690696031398712222269202465612172764701873100593578934114876485676535451596436893605917865028271711974743528605375716132599545959466134981109742654805237510051779132850313114979768346700265411363857011073430884814159959085079818973673525719434920003660305473783621063663226406155535026802686002900972875320331337910420508752958882395777955568257259699665839830041711159485564697978205137648505957385377103949434396071253352960074613898747018268708687857128705414423021526994959345025788659242306286582748148490349979219823821810841988769133810348829500945105839069739873116476164403683329758084965079833461460382082575624863557429107242949391143842062946904652340183200362126275089354995205525130741613020238805722270885765677754831284722311151170578654432351005866165757195608799991905613269744443687666488358800336141120785799637736635624490018109009200218204937981209000570338110925123688372169756259501277757827980060420521583307224291780305150161897187737782949941838281889804302768262361101840843694492751676517723213853980623513155732592908134952127246551228625761895996070636859442240755111895433414210805042793314513330255297620386429328275818056720658920437292972699097260586831513989824172945128405953159631959880114580707155007250064618882791051699438198190074832728020291641826272969764791925004152944028779434867156752075694971196548477484583594591343498842195911663349051817184168797187849967861796540661596846624390467854689482985981099217305847751437968446030911718363351706558841116267384837027911
Q=79753362573107209509799228410097926384889620576438213362215052171473756307430459152408433350814149706584091876571951284887235064277126641495827973409193716704012150870147214185848800483110687069266512569747579757952211565727987213920637438920087831951645765923094206804760648960879202498157595535193709068393089137802589412724302678026238613793887604145734569174313713198739953377936298682747898015663432328978698171791910626382748380220822295614224129116561212808962487296386564457130512195715363291161032031165007219817920315541384768096489218077654714102910152236369985820933265711472229993649893223482246747381128198918937352311862774179432247670603959790468720293068277034864161977138055435066744898081464508970435314820913279625160558483706709447379218277189660598488315527384340733381938680911633324370135247660754082081387709839508531160613149771486533358274504817408245924808714913420225572587464236563615983108478208774317727973470714021021851559144292795951034508587424336161769488215363196315238408961647638132178047797855820061760251743338950556178170427457223551609273876216106384801412224766794549836925176707080278222620000507651531804751168000177958538519875184962922975553241321671788253074205140833507272415823789223806306634461380570141331930582835911028008617337402891826418393100198154834708506575940221111551018310501730846351290266223454480013794415403338805473401347871414968970334944651547432478031861199070258906279725479763676455223652608856981185442616010536993231272467027480461140823161766099586475616859312453115382779217806711430339207442715435819259232426313973745316024590445850279915328858847013073505892218467067847476856399821301628351739134256182240183312806255609668333419763563900470575061210243751784836063658448735569913788353700139189935319933480110899524494453335651350222375437127986970685137001821502339173990972957595887087262216546232606129324076865174199885705155396742113396417200190489209143710622934295814468423610008084394340484993974524478539208286645204672249753280570546361961976244193285344857009664434748039667581760075862569394247419495855722405754779602192594457339550019438422511733366787616736000123410436963028073836597376227990729499560294712271274324697121676240698227071322410288088938572594926421220784879762538610193856649011268350214220547900136154973433294491448167693692125600288517463748865491053725603656612626988915036122885860440646973302114290330423600339917846185137293378677685181668927842388656443469006148620751650438294044727975137286759512131745467958597468196686002775436374481484637433307520421907596397256208004349627743365952374437153890227642517957465553788184710458392259192376659836822995282656300546597924442979298585031805929106783730341257849068015108690027493289132119178496577202228071957666972649749599209335097607090640255720945596138435628328907965816888963796480807930116429662400876110126846483447630830136218138259961508200067150310786378063149952097746643257294677824465157840323367537181862863982092513371672487922719814966295077593675257088532373795072598657765947699306286672123300762130652312847873644138830009521295541018082982584952435172271774412382522950569885273652291939373229761053644252725848129710585108181652151627198671904779861303685054124595499439044602967661872655081294702775440005037488794792505146885522687358721262692029687939790927465320971779979081766576102654573062915553153678173630881977977568560216348028669557848221933172527596696568221946738913846696053707518677816442257600772573350167383873618856518990067331830398835088647110958398612100715523469192870109420130764508873262687056661671892809556789591518002679307636429991706789369397533654884567267768960490535614174881058642365440558572066874089627936066003196018692881065325135151390972019261162476827283472706218172180375489186147637003373429927968993185586335367699051980798656169624768716869814315967621059451370560920190583347436259031676293168750030729849164999370719005827160693955333278046558626424647086569782883840061697709258140227799122953280647180300137833528254904116442883901967825733585921779365414961431425723629295688239141923225292386281791145649064637225754382392777656508495714616011091096757646608843655349591211486579555269016884446364271249589226720704001274379499793805258511502851376139545184523593789921553078479218218500000
```

**Reproduction and limits.** From the active notebook run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/affine_sign_remaining_modes.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_affine_sign_remaining_modes.py

Full certificates are
`scripts/finite-support/affine-sign-remaining-modes-results.json` and
`scripts/finite-support/affine-sign-remaining-modes-verification.json`.
All 1597 construction checks and 318 independent substitution checks
pass, with no failures. The latter invokes neither the constructor nor
an optimizer. It reconstructs the original bounds from the ancestral
source cross/inverse/forced data and original beta coefficients, checks
every original/raw remainder and range, and verifies the entire negative
set. Mode (0,8)'s required lower bound is zero, whereas its actual scaled
and raw remainders are strictly negative. The most negative scaled mode
is (8,1), in [-7561447077392486,-7561447077392485)/10^6; the simpler
(0,8) certificate suffices for rejection.

This is arithmetic verification within one attempt, not the later
dedicated critical proof review. Only the complete fixed (t,z) witness
is rejected. A different z at the same t remains untested. Sign-only
exclusion remains stopped by L086; ATTEMPTS/067–069 and all earlier
fixed-point/weight obstructions remain intact. Scalar upper rows,
other anchors, global consistency, other base/pairs/family choices and
RS realization remain unresolved. There was no optimization, point
scan, retuning, second candidate or new separator.

**Separate critical proof review — step 314, 2026-10-18.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-affine-sign-remaining-modes-critical-audit.md`.
Reuse the precise Schrijver, Sano and Polak imports above. The retained
layers lie in the source ranges on ground sets 68 and 956; finite real
symmetric matrices satisfy Sano's finite-dimensional hypotheses. The
assignment is already invariant and no labeled restriction is averaged.
The suspect complement prefactor is unused. This review establishes the
finite substitution verdict, without recursively approving the ancestral
PSD, uniqueness, whole-kernel or source-decomposition inputs.

Reproduce from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_affine_sign_remaining_modes.py

The complete evidence is
`scripts/finite-support/affine-sign-remaining-modes-critical-audit.json`.
All 7993 checks pass, with no failures. The audit invokes no constructor,
optimizer, point scan, retuning or weight search and changes no earlier
certificate. It consumes the complete step-308 witness, step-310 audit
and original reconstruction, and both step-312 certificates, checking
all input bindings and every relevant coordinate rather than verdicts
or check counts alone.

It reconstructs the original pair equations, positive rho and p8, the
seven-column parameters and RREF, and the original 35 defining completion
rows with the fixed zero coordinate. These yield exactly the immutable
270-entry dictionary. The eight-column RREF reconstructs all 85 affine
factors, all 150 column entries and every coefficient of the 90 original
equations and 90 weighted kernel equations. The full 49-coordinate
witness and all 45 raw moments agree with the previously audited arrays;
all domain/sign controls remain valid. Direct construction of actual
68-element supports and point-by-point membership counts recovers all
500 types and 3000 presentations, 36 forced entries and 45 distinct
free keys, including Boolean cases, forbidden zeros and reanchorings
outside the retained layers.

For an independent normalization check, exact Gram–Schmidt on the powers
1,i,...,i^l with weights C(8,i)C(n-8,l-i) regenerates all eight monic
factor bases for n=68,956 and l=5,6,7,8. Their positive norms and all
coordinates agree with the reviewed direct-action data. Four-region
subset counting rebuilds every entry of all 220 transition matrices in
both rectangular orientations. Every action, absent-mode zero, signed
beta ratio and reference-eight triangle identity agrees. Thus one
positive diagonal congruence relates each entire weighted block to its
source block, including the anchor correction; no pseudoinverse
congruence is presumed.

All 306 old principal minors are recomputed. Fresh Cramer solves on
largest nonsingular principal subsystems check every original inverse
row, while reverse-order elimination of the direct weighted blocks
independently verifies all zero-pivot rows/cross entries and energies.
The rank distributions for old-layer counts 3,2,1,0 are respectively
(19,8,4,5), (3,3,7), (4,11), (17), ordered by increasing rank. Thus all
36,13,15,17 cases are retained. All affine inverse residuals also vanish.
Every positive multiplicity is checked and their sums recover each
layer's full dimension.

All original free coefficients, forced terms, full anchor subtractions,
bounds and costs agree. For every one of the 81 modes the direct weighted
remainder divided by p8 times the product norm, the original scaled
slack, and the raw remainder divided by p8*D_i are exactly equal.
The complete sign partition is precisely the 19 negative indices above,
34 positive indices and 28 selected zeros. Neither a numerical tolerance
nor sign assumptions on the free variables supply this negative verdict.

For a further independent check of (0,8), set

    E_(n,a)(r)=sum_(h=0)^r (-1)^h C(a,h)C(8-a,r-h)C(n-8-a,r-h).

The audit evaluates the complete 81-term finite sum

    sum_(r,q=0)^8 E_(68,0)(r)E_(956,8)(q)Y_88(8-r,8-q)/p8.

It equals sigma_8 exactly, independently of every old inverse. All its
terms are saved in `new_only_0_8_terms`. Parsing the entire N and Q in
this manuscript gives exactly the reduced numerator and denominator of
that sum, with N<0 and Q>0. Integer comparisons verify the displayed
interval, and the positive raw multiplier equals exactly
46806225362314/445376358283605. In direct coordinates the product of the
degree-zero head basis and degree-eight tail basis, supported only on
layer eight, has positive squared norm N8 and quadratic form
N8*p8*sigma_8<0. This is the concrete negative direction of the same
new-only mode, with no singular inverse or anchor ambiguity.

The critical audit therefore retains rejection of this complete fixed
(t,z) assignment only. Different 45-moment assignments at the same t,
other plane points, other anchors, global consistency and RS realization
remain unresolved. L086's sign/equality pass, both conic stops and the
955–957 bracket are unchanged. This is a reviewed local reproduction of
assessed tools, not a new source-level theorem or an RS safety result.

## Mathlib

Full matching fixed-witness mode verdict: not checked. Supporting
mixed-layer decomposition, singular Schur complement and exact rational
linear algebra coverage: not checked here. Unknown coverage is not
evidence of absence. Known tools are imported by the precise citations
above; this finite specialization makes no novelty claim.
