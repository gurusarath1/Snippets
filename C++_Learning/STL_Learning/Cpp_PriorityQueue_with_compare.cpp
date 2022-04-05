    class Compare
    {
    public:
        bool operator() (pair<double,int> a, pair<double,int> b)
        {
            return a.first > b.first;
        }
    };
    
    
    priority_queue<pair<double, int>, vector<pair<double, int>>, Compare> pq;




class Foo
{

};

bool Compare(Foo, Foo)
{
    return true;
}

int main()
{
    std::priority_queue<Foo, std::vector<Foo>, std::function<bool(Foo, Foo)>> pq(Compare);
    return 0;
}
