//
// Created by netherblood on 16.04.17.
//
#include <stdio.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int calc_group(int* votes, int votes_count) {
    int start;
    int end;
    int x;
    scanf("%d %d %d", &start, &end, &x);
//    printf("START: %d\n", start);
//    printf("END: %d\n", end);
//    printf("X: %d\n", x);
    int* curr_votes = malloc(sizeof(int) * votes_count);
    // nullify votes
    for (int k = 0; k < votes_count; ++k) {
        curr_votes[k] = 0;
    }
    for (int i = start; i <= end; i++) {
//        printf("Guy i:%d votes for %d\n", i, votes[i]);
        curr_votes[votes[i]] += 1;
    }

    int min_idx = INT_MAX;
    for (int j = 0; j < votes_count; j++) {
        if (curr_votes[j] == x) {
//            printf("Found X %d AT J: %d\n", x, j);
            min_idx = j;
            break;
        }
    }

    free(curr_votes);
    if (min_idx == INT_MAX) {
        return -1;
    }
    return min_idx;
}

int main() {
    int test_case_count;
    scanf("%d", &test_case_count);

    for (int i = 0; i < test_case_count; i++) {
        int vote_count;
        scanf("%d\n", &vote_count);

        int* votes = malloc(sizeof(int) * vote_count);
        // nullify votes
        for (int k = 0; k < vote_count; ++k) {
            votes[k] = 0;
        }
        // read votes
        for (int v_idx = 0; v_idx < vote_count; ++v_idx) {
            scanf("%d", &votes[v_idx]);
//            printf("Guy i:%d votes for %d\n", v_idx, votes[v_idx]);
        }

        int group_count;
        scanf("%d", &group_count);
        for (int j = 0; j < group_count; ++j) {
            printf("%d\n", calc_group(votes, vote_count));
        }
        free(votes);
    }
}