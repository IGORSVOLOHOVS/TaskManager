#include <iostream>


template <typename... T>
void read(T ...args) {
    ((std::cin >> args), ...);
}


template <typename... T>
void write(std::string delimiter, T &&...args) {
    ((std::cout << args << delimiter), ...);
}


template <typename T>
void readContainer(T &t) {
    for (auto &e : t) {
        read(e);
    }
}


template <typename T>
void writeContainer(std::string delimiter, T &t) {
    for (const auto &e : t) {
        write(delimiter, e);
    }
    write("\n");
}

//     // Question: read three space seprated integers and print them in different lines.
// 	int x, y, z;
// 	read(x, y, z);
// 	write("\n", x, y, z);
	
// // even works with variable data types :)
// 	int n;
// 	string s;
// 	read(n, s);
// 	write(" ", s, "has length", n, "\n");
	
// // Question: read an array of `N` integers and print it to the output console.
// 	int N;
// 	read(N);
// 	vector<int> arr(N);
// 	readContainer(arr);
// 	writeContainer(" ", arr); // output: arr[0] arr[1] arr[2] ... arr[N - 1]
// 	writeContainer("\n", arr);
// 	/**
// 	* output:
// 	* arr[0]
// 	* arr[1]
// 	* arr[2]
// 	* ...
// 	* ...
// 	* ...
// 	* arr[N - 1]
// 	*/
