// Bounded deterministic discovery for the frozen length-16 RS model.
// A candidate must be checked independently against the original event.
#include <array>
#include <cstdint>
#include <iostream>
#include <utility>

using Word = std::array<int, 16>;
using Syndrome = std::array<int, 8>;
int inv[17], powers[17][9];
std::uint64_t state = 2026092509ULL;

std::uint64_t random_word() {
    state ^= state << 13;
    state ^= state >> 7;
    state ^= state << 17;
    return state;
}

int mod(int value) {
    int result = value % 17;
    return result < 0 ? result + 17 : result;
}

Syndrome syndrome(const Word &word) {
    Syndrome result{};
    for (int j = 0; j < 8; ++j)
        for (int x = 1; x <= 16; ++x)
            result[j] = (result[j] + word[x - 1] * powers[x][j + 1]) % 17;
    return result;
}

// Berlekamp--Massey on eight moments, followed by a split-root test.
// The resulting support is independently checked by interpolation in check.py.
unsigned decode_support(const Syndrome &s) {
    std::array<int, 9> c{}, b{};
    c[0] = b[0] = 1;
    int length = 0, shift = 1, previous = 1;
    for (int n = 0; n < 8; ++n) {
        int discrepancy = s[n];
        for (int j = 1; j <= length; ++j)
            discrepancy += c[j] * s[n - j];
        discrepancy %= 17;
        if (discrepancy == 0) {
            ++shift;
            continue;
        }
        auto old = c;
        int coefficient = discrepancy * inv[previous] % 17;
        for (int j = 0; j + shift <= 8; ++j)
            c[j + shift] = mod(c[j + shift] - coefficient * b[j]);
        if (2 * length <= n) {
            length = n + 1 - length;
            if (length > 4) return 0;
            b = old;
            previous = discrepancy;
            shift = 1;
        } else {
            ++shift;
        }
    }
    if (length == 0) return 1U << 16; // sentinel for the zero error
    unsigned mask = 0;
    int count = 0;
    for (int x = 1; x <= 16; ++x) {
        int value = c[length];
        for (int j = length - 1; j >= 0; --j)
            value = (value * inv[x] + c[j]) % 17;
        if (value == 0) {
            mask |= 1U << (x - 1);
            ++count;
        }
    }
    return count == length ? mask : 0;
}

void print_word(const char *label, const Word &word) {
    std::cout << label << " = [";
    for (int i = 0; i < 16; ++i) std::cout << (i ? ", " : "") << word[i];
    std::cout << "]\n";
}

int main() {
    for (int x = 1; x <= 16; ++x) {
        powers[x][0] = 1;
        for (int j = 1; j <= 8; ++j) powers[x][j] = powers[x][j - 1] * x % 17;
        for (int y = 1; y <= 16; ++y) if (x * y % 17 == 1) inv[x] = y;
    }
    int best = 0;
    const int limit = 500000;
    for (int trial = 1; trial <= limit; ++trial) {
        std::array<int, 16> points{};
        for (int i = 0; i < 16; ++i) points[i] = i;
        for (int i = 0; i < 8; ++i)
            std::swap(points[i], points[i + random_word() % (16 - i)]);
        Word a{}, other{}, direction{};
        unsigned mask0 = 0, mask1 = 0;
        for (int i = 0; i < 4; ++i) {
            a[points[i]] = 1 + random_word() % 16;
            other[points[i + 4]] = 1 + random_word() % 16;
            mask0 |= 1U << points[i];
            mask1 |= 1U << points[i + 4];
        }
        for (int i = 0; i < 16; ++i) direction[i] = mod(other[i] - a[i]);
        Syndrome start = syndrome(a), step = syndrome(direction), current{};
        for (int j = 0; j < 8; ++j) current[j] = (start[j] + step[j]) % 17;
        std::array<unsigned, 17> supports{};
        supports[0] = mask0;
        supports[1] = mask1;
        int count = 2;
        for (int gamma = 2; gamma < 17; ++gamma) {
            for (int j = 0; j < 8; ++j) current[j] = (current[j] + step[j]) % 17;
            supports[gamma] = decode_support(current);
            if (supports[gamma]) ++count;
        }
        if (count > best) {
            best = count;
            std::cout << "trial " << trial << ": " << count << " decodable parameters\n";
            std::cout.flush();
        }
        if (count >= 7) {
            print_word("a", a);
            print_word("b", direction);
            for (int gamma = 0; gamma < 17; ++gamma) if (supports[gamma]) {
                std::cout << gamma << ":";
                for (int i = 0; i < 16; ++i) if (supports[gamma] & (1U << i))
                    std::cout << " " << i + 1;
                std::cout << "\n";
            }
            return 0;
        }
    }
    std::cout << "Search exhausted " << limit << " trials; best = " << best << ".\n";
    return 0;
}
