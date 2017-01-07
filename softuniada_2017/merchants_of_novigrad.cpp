#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

class Vertex;

const int WHITE = 0, GRAY = 1, BLACK = 2;
// WHITE: unseen, GRAY: in the current path, BLACK: finished (num paths known)
const int CYCLE = -1;
struct Triplet
{
  long long pthz;
  bool hloop;
};

class Vertex
{
public:
    long long paths;
    int color;
    bool hasLoop;
    vector<Vertex *> nbrs;

    Vertex();
    vector<Triplet> countPaths();
};

 


Vertex::Vertex()
{
    paths = 0;
    color = WHITE;
    hasLoop = false;
}

vector<Triplet> Vertex::countPaths()
{
  vector<Triplet> result;
    // sets this->paths to the number of paths, or CYCLE (-1) for cycles
    // returns this->paths

    if (color == BLACK)
    {
        // paths already calculated, no need to do anything
    }
    else if (color == GRAY)
    {
        // detected a loop
        hasLoop = true;
    }
    else if (color == WHITE)
    {
        // recursively find all the paths from the neighbours
        color = GRAY;
        for (unsigned int i = 0; i < nbrs.size(); i++)
        {
            nbrs[i]->countPaths()[0].pthz;
            if (nbrs[i]->paths == CYCLE)
            {
                // found cycle, no point continuing
                paths = CYCLE;
                break;
            }
            paths += nbrs[i]->paths;
        }
        color = BLACK;

        // check if some other node found a cycle to 'this'
        if (hasLoop && paths > 0) paths = CYCLE;
    }
    Triplet tr;
    tr.pthz = paths;
    tr.hloop = hasLoop;
result.push_back (tr);

    return result;
}
int main()
{
    int numverts, numedges;
    Vertex** verts; // dynamically-allocated array of Vertex*
    scanf("%d %d", &numverts, &numedges);

    verts = new Vertex*[numverts+1];
    for (int i = 0; i < numverts + 1; i++) verts[i] = new Vertex();

    for (int i = 0; i < numedges; i++)
    {
        int a, b;
        scanf("%d %d", &a, &b);
        verts[a]->nbrs.push_back(verts[b]);
    }

    verts[numverts]->paths = 1; // the base case
    
    vector<Triplet> a = verts[1]->countPaths();
    long long numPaths = a[0].pthz;
    bool hasLoop = a[0].hloop;
    // free dynamic memory, set pointers to NULL to prevent accidents
    for (int i = 0; i < numverts; i++) { delete verts[i]; verts[i] = NULL; }
    delete[] verts; verts = NULL;

    if (numPaths == CYCLE) printf("infinite \n");
    else if (hasLoop == true) printf("%lld yes\n", numPaths);
    else printf("%lld no\n", numPaths);

    return 0;
}
