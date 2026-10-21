// Independent of the producer's Plucker keys: affine directions at every anchor.
// Input: number of configurations, then mask, point count, and five coordinates.
#include <array>
#include <iostream>
#include <map>
#include <stdexcept>
#include <unordered_map>
#include <vector>

constexpr int prime = 97;
using Point = std::array<int, 5>;
void require(bool ok) { if (!ok) throw std::runtime_error("anchor census invariant failed"); }
int mod(int x) { return (x % prime + prime) % prime; }
int power(int x, int exponent) {
    int answer = 1;
    while (exponent) {
        if (exponent & 1) answer = answer * x % prime;
        x = x * x % prime;
        exponent >>= 1;
    }
    return answer;
}
void histogram(const std::map<int, int>& values) {
    std::cout << '{';
    bool comma = false;
    for (auto [size, count] : values) {
        if (comma) std::cout << ',';
        std::cout << '"' << size << "\":" << count;
        comma = true;
    }
    std::cout << '}';
}
int main() {
    std::array<int, prime> inverses{};
    for (int x = 1; x < prime; ++x) {
        inverses[x] = power(x, prime - 2);
        require(x * inverses[x] % prime == 1);
    }
    int configurations;
    require(bool(std::cin >> configurations));
    require(configurations == 273);
    for (int configuration = 0; configuration < configurations; ++configuration) {
        int mask, n;
        require(bool(std::cin >> mask >> n));
        require(n == 330);
        std::vector<Point> points(n);
        for (auto& point : points) {
            for (auto& x : point) {
                require(bool(std::cin >> x));
                require(0 < x && x < prime);
            }
            require(point[0] == 1);
        }
        std::map<int, int> anchored_histogram;
        std::cout << "{\"mask\":" << mask << ",\"anchors\":[";
        for (int i = 0; i < n; ++i) {
            std::unordered_map<unsigned, int> directions;
            directions.reserve(400);
            for (int j = 0; j < n; ++j) {
                if (j == i) continue;
                std::array<int, 4> difference{};
                int pivot = -1;
                for (int k = 0; k < 4; ++k) {
                    difference[k] = mod(points[j][k + 1] - points[i][k + 1]);
                    if (pivot < 0 && difference[k]) pivot = k;
                }
                require(pivot >= 0);
                const int inverse = inverses[difference[pivot]];
                unsigned key = 0;
                for (int x : difference) key = key * prime + x * inverse % prime;
                ++directions[key];
            }
            std::map<int, int> local;
            int neighbors = 0;
            for (auto [key, count] : directions) {
                ++local[count + 1];
                ++anchored_histogram[count + 1];
                neighbors += count;
            }
            require(neighbors == 329);
            if (i) std::cout << ',';
            histogram(local);
        }
        std::map<int, int> lines;
        int pairs = 0;
        for (auto [size, count] : anchored_histogram) {
            require(count % size == 0);
            lines[size] = count / size;
            pairs += lines[size] * size * (size - 1) / 2;
        }
        require(pairs == 54285);
        std::cout << "],\"line_size_histogram\":";
        histogram(lines);
        std::cout << ",\"maximum_external_points\":" << lines.rbegin()->first
                  << ",\"directed_differences\":" << n * (n - 1) << "}\n";
    }
    std::cin >> std::ws;
    require(std::cin.eof());
}
