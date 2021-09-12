    class Compare
    {
    public:
        bool operator() (pair<double,int> a, pair<double,int> b)
        {
            return a.first > b.first;
        }
    };
    
    
    priority_queue<pair<double, int>, vector<pair<double, int>>, Compare> pq;
