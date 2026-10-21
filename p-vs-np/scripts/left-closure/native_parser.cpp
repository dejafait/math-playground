// Exact ASCII native syntax parser. Hash-table collisions use full key equality.
// No proof rules, semantic evaluation, or string hashes are accepted as evidence.
#include <cstdint>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

struct Node { int tag, a, b; std::string name; };
struct Key {
    int tag, a, b; std::string name;
    bool operator==(const Key& k) const {
        return tag==k.tag && a==k.a && b==k.b && name==k.name;
    }
};
struct Hash {
    size_t operator()(const Key& k) const {
        size_t h=std::hash<std::string>{}(k.name);
        for (int x : {k.tag,k.a,k.b}) h=(h*1000003)^std::hash<int>{}(x);
        return h;
    }
};
struct Pool { std::vector<Node> nodes; std::unordered_map<Key,int,Hash> ids; };
static thread_local std::string error;
static bool alnum(char c) {
    return (c>='A'&&c<='Z') || (c>='a'&&c<='z') ||
           (c>='0'&&c<='9') || c=='_';
}
static int intern(Pool& p,int tag,int a,int b,const std::string& name) {
    Key k{tag,a,b,name};
    auto it=p.ids.find(k);
    if (it!=p.ids.end()) return it->second;
    int id=static_cast<int>(p.nodes.size());
    p.nodes.push_back(Node{tag,a,b,name}); p.ids.emplace(std::move(k),id);
    return id;
}
struct Parser {
    Pool& pool; const char* s; size_t len, pos=0;
    void want(char c) {
        if (pos>=len || s[pos]!=c) throw std::runtime_error("wrong native connective/parenthesis");
        ++pos;
    }
    int term(unsigned depth=0) {
        // A practical receiving limit: reject rather than overflow the C stack.
        if (depth>4096) throw std::runtime_error("native parser depth resource limit");
        if (pos>=len) throw std::runtime_error("unexpected native syntax end");
        if (s[pos]!='(') {
            size_t begin=pos;
            while (pos<len && alnum(s[pos])) ++pos;
            if (pos==begin) throw std::runtime_error("bad ASCII variable");
            return intern(pool,0,-1,-1,std::string(s+begin,pos-begin));
        }
        ++pos;
        int id;
        if (pos<len && s[pos]=='~') {
            ++pos; int a=term(depth+1); want(')'); id=intern(pool,1,a,-1,"");
        } else {
            int a=term(depth+1); want('>'); int b=term(depth+1);
            want(')'); id=intern(pool,2,a,b,"");
        }
        return id;
    }
};
extern "C" {
void* parser_new() { return new Pool; }
void parser_free(void* p) { delete static_cast<Pool*>(p); }
const char* parser_error() { return error.c_str(); }
int parser_parse(void* raw,const char* s,size_t n) {
    try {
        Parser parser{*static_cast<Pool*>(raw),s,n}; int id=parser.term();
        if (parser.pos!=n) throw std::runtime_error("trailing native syntax");
        return id;
    } catch (const std::exception& e) { error=e.what(); return -1; }
}
int parser_node(void* raw,int tag,int a,int b,const char* name) {
    auto& p=*static_cast<Pool*>(raw);
    try {
        if (tag==0) {
            if (!name || !*name) throw std::runtime_error("empty variable");
            for (const char* c=name;*c;++c) if (!alnum(*c)) throw std::runtime_error("bad ASCII variable");
        } else if ((tag!=1 && tag!=2) || a<0 || size_t(a)>=p.nodes.size() ||
                   (tag==2 && (b<0 || size_t(b)>=p.nodes.size()))) {
            throw std::runtime_error("invalid structural node");
        }
        return intern(p,tag,a,b,tag==0 ? name : "");
    } catch (const std::exception& e) { error=e.what(); return -1; }
}
size_t parser_count(void* raw) { return static_cast<Pool*>(raw)->nodes.size(); }
struct Info { int tag,a,b; const char* name; };
Info parser_info(void* raw,size_t i) {
    const auto& n=static_cast<Pool*>(raw)->nodes.at(i);
    return Info{n.tag,n.a,n.b,n.name.c_str()};
}
}
