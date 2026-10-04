// Exact finite configuration over F_97; no enumeration of extension weights.
// One JSON record per multiplicative orbit of five-coordinate sets.
#include <array>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

constexpr int prime = 97;
using Point = std::array<int, 5>;
using Support = std::array<int, 4>;
struct Entry { int pairs = 0; int first = -1; int second = -1; };

void require(bool condition) { if (!condition) std::abort(); }
int mod(int value) { value %= prime; return value < 0 ? value + prime : value; }
int rotate_mask(int mask, int shift) {
    return ((mask << shift) | (mask >> (16 - shift))) & 65535;
}
template <typename Container> void print_array(const Container& values) {
    std::cout << '[';
    bool comma = false;
    for (int value : values) {
        if (comma) std::cout << ',';
        std::cout << value;
        comma = true;
    }
    std::cout << ']';
}

int main() {
    std::array<int, 97> inverse{};
    for (int i = 1; i < prime; ++i) {
        for (int j = 1; j < prime; ++j) {
            if (i * j % prime == 1) inverse[i] = j;
        }
        require(inverse[i] != 0);
    }
    std::array<int, 16> domain{};
    domain[0] = 1;
    for (int i = 1; i < 16; ++i) domain[i] = 8 * domain[i - 1] % prime;
    require(8 * domain[15] % prime == 1);
    require(std::set<int>(domain.begin(), domain.end()).size() == 16);
    int orbits = 0;
    for (int mask = 0; mask < 65536; ++mask) {
        if (__builtin_popcount(static_cast<unsigned>(mask)) != 5) continue;
        bool representative = true;
        for (int shift = 1; shift < 16; ++shift) {
            int rotated = rotate_mask(mask, shift);
            require(rotated != mask); // Five is coprime to every nontrivial orbit size.
            if (rotated < mask) representative = false;
        }
        if (!representative) continue;
        ++orbits;
        std::vector<int> a, j;
        for (int i = 0; i < 16; ++i) {
            (mask & (1 << i) ? a : j).push_back(domain[i]);
        }
        require(a.size() == 5 && j.size() == 11);
        std::vector<Point> points;
        std::vector<Support> supports;
        for (int i0 = 0; i0 < 8; ++i0)
        for (int i1 = i0 + 1; i1 < 9; ++i1)
        for (int i2 = i1 + 1; i2 < 10; ++i2)
        for (int i3 = i2 + 1; i3 < 11; ++i3) {
            Support c{j[i0], j[i1], j[i2], j[i3]};
            Point point{};
            for (int x = 0; x < 5; ++x) {
                point[x] = 1;
                for (int y = 0; y < 11; ++y) {
                    if (y != i0 && y != i1 && y != i2 && y != i3)
                        point[x] = point[x] * mod(a[x] - j[y]) % prime;
                }
                require(point[x] != 0);
            }
            int scale = inverse[point[0]];
            for (int& value : point) value = value * scale % prime;
            points.push_back(point);
            supports.push_back(c);
        }
        require(points.size() == 330);
        require(std::set<Point>(points.begin(), points.end()).size() == 330);
        std::unordered_map<std::string, Entry> lines;
        lines.reserve(55000);
        for (int i = 0; i < 330; ++i) for (int k = i + 1; k < 330; ++k) {
            std::array<int, 10> minors{};
            int offset = 0, scale = 0;
            for (int x = 0; x < 5; ++x) for (int y = x + 1; y < 5; ++y) {
                int value = mod(points[i][x] * points[k][y] - points[i][y] * points[k][x]);
                minors[offset++] = value;
                if (scale == 0 && value != 0) scale = inverse[value];
            }
            require(scale != 0);
            std::string key;
            for (int value : minors) key.push_back(static_cast<char>(value * scale % prime));
            Entry& entry = lines[key];
            if (entry.pairs == 0) { entry.first = i; entry.second = k; }
            ++entry.pairs;
        }
        int maximum = 0, total_pairs = 0;
        std::map<int, int> histogram;
        std::string best_key;
        Entry best;
        for (const auto& item : lines) {
            const Entry& entry = item.second;
            int count = 2;
            while (count * (count - 1) / 2 < entry.pairs) ++count;
            require(count * (count - 1) / 2 == entry.pairs);
            ++histogram[count];
            total_pairs += entry.pairs;
            if (count > maximum || (count == maximum && item.first < best_key)) {
                maximum = count; best_key = item.first; best = entry;
            }
        }
        require(total_pairs == 54285);
        const Point& p = points[best.first];
        const Point& q = points[best.second];
        int pivot = 1;
        while (pivot < 5 && p[pivot] == q[pivot]) ++pivot;
        require(pivot < 5);
        std::vector<int> collinear;
        for (int i = 0; i < 330; ++i) {
            int parameter = mod(points[i][pivot] - p[pivot]) * inverse[mod(q[pivot] - p[pivot])] % prime;
            bool on_line = true;
            for (int x = 0; x < 5; ++x)
                if (points[i][x] != mod(p[x] + parameter * (q[x] - p[x]))) on_line = false;
            if (on_line) collinear.push_back(i);
        }
        require(static_cast<int>(collinear.size()) == maximum);
        std::cout << "{\"mask\":" << mask << ",\"A\":";
        print_array(a);
        std::cout << ",\"distinct_points\":330,\"pairs\":54285,\"lines\":" << lines.size()
                  << ",\"maximum_external_points\":" << maximum << ",\"line_size_histogram\":{";
        bool comma = false;
        for (const auto& item : histogram) {
            if (comma) std::cout << ',';
            std::cout << '"' << item.first << "\":" << item.second;
            comma = true;
        }
        std::cout << "},\"maximum_line_plucker\":";
        std::vector<int> key_values;
        for (unsigned char value : best_key) key_values.push_back(value);
        print_array(key_values);
        std::cout << ",\"maximum_line_supports\":[";
        comma = false;
        for (int i : collinear) {
            if (comma) std::cout << ',';
            print_array(supports[i]); comma = true;
        }
        std::cout << "]}" << '\n';
    }
    require(orbits == 273);
}
