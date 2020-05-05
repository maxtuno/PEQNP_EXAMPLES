g++ validate_clique.cpp -std=c++11 -o validate_clique
gcc generator.c -o generator

./generator data.clq 100

python3 k-clq.py data.clq 10

solution format for a k clique:
k
i_1, i_2, ..., i_k