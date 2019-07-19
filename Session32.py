"""
    UNSUPERVISED LEARNING
    We have Data but we have no label

    k-means clustering :)
    k denotes number of classes which we want to achieve


    ----------
    X   Y   P
    ----------
    1   1   A
    1   0   B
    0   2   C
    2   4   D
    3   5   E
    ----------

    Step 1:
    Assume 2 Centroids randomly for 2 Classes
    eg: A(1, 1) and C(0, 2)

    Step 2:
    Compute distance of All the Points from Centroids
    Eucilidean Distance Formula : sqrt[ sq(x2-x1) + sq(y2-y1)]

    ------------------------
    P   C1(1, 1)   C2(0, 2)
    ------------------------
    A      0          1.4
    B      1          2.2
    C     1.4          0
    D     3.2         2.8
    E     4.5         4.2
    ------------------------

    Step 3:
    Arrange Points as per distance from Centroids

    ----------------
    P   Nearest To
    ----------------
    A       C1
    B       C1
    C       C2
    D       C2
    E       C2
    ----------------

    Step 4:
    Re-check again with new Centroids of the created new clustures

    -------------------------
    X   Y   P   Nearest To
    -------------------------
    1   1   A       C1
    1   0   B       C1
    0   2   C       C2
    2   4   D       C2
    3   5   E       C2
    -------------------------

    Clusture Mean

    CM1 = (1 + 1)/2, (1 + 0)/2
        = (1, .5)
    CM2 = (0 + 2 + 3)/3, (2 + 4 + )/3
        = (1.7, 3.7)

    --------------------------------
    P   CM1(1, .5)   CM2(1.7, 3.7)
    --------------------------------
    A       0.5            2.7
    B       0.5            3.2
    C       1.8            2.4
    D       3.6            0.5
    E       4.9            1.9
    --------------------------------

    -------------------------
    X   Y   P   Nearest To
    -------------------------
    1   1   A       CM1
    1   0   B       CM1
    0   2   C       CM1
    2   4   D       CM2
    3   5   E       CM2
    -------------------------

    Redo the same steps till we do not get the same custures :)

    -------------------------
    X   Y   P   Nearest To
    -------------------------
    1   1   A       CM1
    1   0   B       CM1
    0   2   C       CM1
    2   4   D       CM2
    3   5   E       CM2
    -------------------------

    Clusture Mean

    CM1 = (1 + 1 + 0)/3, (1 + 0 + 2)/3
        = (0.6, 1)
    CM2 = (2 + 3)/2, (4 + 5)/2
        = (2.5, 4.5)

    --------------------------------
    P   CM1(0.6, 1)   CM2(2.5, 4.5)
    --------------------------------
    A       0.4            2.7
    B       0.5            3.2
    C       1.8            2.4
    D       3.6            0.5
    E       4.9            1.9
    --------------------------------

    -------------------------
    X   Y   P   Nearest To
    -------------------------
    1   1   A       CM1
    1   0   B       CM1
    0   2   C       CM1
    2   4   D       CM2
    3   5   E       CM2
    -------------------------

"""

import matplotlib.pyplot as plt
X = [1, 1, 0, 2, 3]
Y = [1, 0, 2, 4, 5]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.scatter(X, Y)
plt.title("k-means")
plt.show()