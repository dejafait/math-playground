# Guarded postspell descent: least-root applicability

The completed target is the exact COVERED_TARGET in
drafts/literature/2026-10-04-residue47-bounded-ancestor-cover.md. Reuse
that prior IMPORT assessment unchanged. Its inspected forward theorem
is the mathematical input by citation; no further source review or
reproof of its original-root margin is needed.

The main gap is convergence on the infinite least-root domain surviving
L014–L018. The intermediate target is a necessary upper bound on the
final binary valuation after an actual prefix (OOEO)^J O^H, with J>=2
and H>=3, at the fixed least nonconvergent residue-20 root. Its possible
later use is to isolate the insufficient-halving cases that a further
excursion or descent argument would have to handle. Entry into this
prefix class and those remaining cases are separate unresolved steps.

The discriminating test is whether the cited guard supplies an actual
iterate m>0 in residue 20 modulo 27 with m strictly below the original
root. An algebraic endpoint without actual parities, a smaller integer
outside the target set, or a comparison with a later larger return
would fail this test. The imported threshold is sufficient and is not
asserted to be optimal.

## Applicability argument saved before checks

Use O(x)=(3x+1)/2 only at odd input and E(x)=x/2 only at even input.
Sodelin, *Guarded root descent after independently unbounded return
spells and odd runs*, node AC-POSTSPELL-GUARDED-ROOT-DESCENT-001,
[sections 1–3 of Postspell_Guarded_Root_Descent.md](https://github.com/Sodelin/Collatz-Conjecture-Work/blob/main/proof-search/lemmas/Postspell_Guarded_Root_Descent.md#1-uniform-original-root-margin),
was inspected in the prior assessment. For an actual prefix
(OOEO)^J O^H from r>3, J>=2 and H>=3, it gives
0<z/2^e<r whenever e>=J+H and 2^e divides the prefix endpoint z.
For a residue-20 root it also gives target membership when e=2 modulo
18. Import these statements at their stated hypotheses.

Set s=J+H and e=s+((2-s) mod 18), with the remainder in {0,...,17}.
Then e is the least integer at least s congruent to 2 modulo 18. If
v_2(z)>=e, every one of the next e inputs is even: for 0<=i<e,
z/2^i is a positive even integer. Therefore m=z/2^e is the actual
(4J+H+e)-th iterate of the original root, not an auxiliary affine
value. The cited margin and residue conclusion give 0<m<r and
m=20 modulo 27.

Apply this at the fixed n=min B_20 supplied by L014. Positive
residue-20 roots satisfy n>=20>3. Minimality makes m convergent;
appending its finite path to 1 to the actual n-to-m path makes n
convergent too. This contradiction requires v_2(z)<e. Forward
convergence transfer needs no ordering of ancestor-hit times.

L014 supplies the least-root premise. L015–L018 restrict its arithmetic
domain but are not used in this implication. Earlier finite-window,
first-return and bounded-ancestor failures do not imply this conditional
whole-excursion restriction; conversely, this restriction establishes no
universal satisfaction of its guard. The already inspected failed-guard
source prevents dropping that qualification.

## Checks and completion

[L019](../lemmas/L019-guarded-postspell-least-root-halving-bound.md)
records the precise cited input and full applicability argument. Exact
checks gave 2^18=1 modulo 27, 16*20=23 modulo 27 and 4*20=26 modulo
27. Three positive residue-20 starts supplied actual guarded words:

| J | H | e | Original root r | Prefix endpoint z | Tail endpoint m | Total time |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 20 | 103791333467 | 997521883136 | 951311 | 31 |
| 3 | 5 | 20 | 5500059268187 | 200703529189376 | 191405801 | 37 |
| 7 | 9 | 20 | 4075760634985280603 | 6105714210454060924928 | 5822862825826703 | 57 |

In each replay, every input parity matched, v_2(z)=e, 0<m<r and
m=20 modulo 27. These are arbitrary test starts, not purported
nonconvergent roots. They check the map, endpoint, time and guard
transcription; the cited theorem supplies the universal size margin.
The starts were constructed by extending the requested parity word
one bit at a time and then imposing residue 20 by CRT. Replay alone
can be reproduced from this directory with:

```bash
python3 - <<'PY'
samples = (
    (2, 3, 103791333467, 997521883136, 951311),
    (3, 5, 5500059268187, 200703529189376, 191405801),
    (7, 9, 4075760634985280603, 6105714210454060924928, 5822862825826703),
)
assert pow(2, 18, 27) == 1
assert 16 * 20 % 27 == 23 and 4 * 20 % 27 == 26
for j, h, root, expected_z, expected_m in samples:
    e = j + h + (2 - j - h) % 18
    assert e >= j + h and e % 18 == 2
    assert all(a % 18 != 2 for a in range(j + h, e))
    prefix = 'OOEO' * j + 'O' * h
    states = [root]
    for symbol in prefix + 'E' * e:
        x = states[-1]
        assert x % 2 == (symbol == 'O')
        states.append(x // 2 if x % 2 == 0 else (3 * x + 1) // 2)
    z, m = states[len(prefix)], states[-1]
    assert (z, m) == (expected_z, expected_m)
    assert (z & -z).bit_length() - 1 == e
    assert root % 27 == m % 27 == 20 and 0 < m < root
print('Three guarded replays and exact modular checks passed.')
PY
```

The completed target is ADVANCE with classification KNOWN_IMPORTED:
a relevant conditional restriction is now assembled locally, without
progress beyond the inspected source. L014 is the only direct local
mathematical input to L019; L015–L018 are context, not premises.
The achieved bound excludes sufficient final-halving guards only for
the specified actual prefixes. The required result is convergence or
eventual descent at every remaining root; neither prefix entry nor
its insufficient-halving complement is covered. No complete candidate
or uniform rank has appeared.

No mathematical EXPLORATION turn was spent and no historical counter
was reset. Attempts 009, 010 and 011 remain parked/stopped. Lowering
the exponent below the imported e changes the theorem's size hypothesis:
an exponent congruent to 2 modulo 18 below e is below J+H. Such a
sharpening is not preapproved by the reused assessment; its pending
REVIEW_REQUIRED record permits no calculation of that new target in
this turn.
