#include <iostream>

using namespace std;

struct point {
    int x;
    int y;
} pk, pk2;


struct point2 {
    int angle;
    int mag;
};


typedef struct point3D {
    int x;
    int y;
    int z;
}point3D;

int main()
{
    
    struct point p1;
    
    point3D p3D;
    
    p1.x = 9;
    p1.y  = 1;
    
    pk.x = 1;
    pk.y =3;
    
    pk2.x = 11;
    pk2.y =32;
    
    p3D.x = 1;
    p3D.y = 2;
    p3D.z = 3;
    
    cout << pk.x << "  " << pk.y << endl;
    
    cout << p3D.x << "  " << p3D.y << "  " << p3D.z << endl;
    
    
    // Struct Pointers ------------------------------
    
    point3D* pp3D;
    
    pp3D = &p3D;
    
    cout << pp3D->x << "  " << pp3D->y << "  " << pp3D->z << endl;
    
    return 0;
}
