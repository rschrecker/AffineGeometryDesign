def AffineGeometryDesign(n, d, F):
    '''
    Return an Affine Geometry Design.
        INPUT:
        * n (integer) -- the Euclidean dimension. The number of points is
          v=|F^n|.

        * d (integer) -- the dimension of the (affine) subspaces of P =
          GF(q)^n which make up the blocks.

        * F -- a Finite Field (i.e. "FiniteField(17)"), or a prime power
          (i.e. an integer)

        AG_{n,d} (F), as it is sometimes denoted, is a 2 - (v, k, lambda)
        design of points and d- flats (cosets of dimension n) in the affine
        geometry AG_n (F), where

            v = q^n,  k = q^d , lambda =frac{(q^{n-1}-1) ...
            (q^{n+1-d}-1)}{(q^{n-1}-1) ... (q-1)}.
        EXAMPLES:
            sage: BD = designs.AffineGeometryDesign(3, 1, GF(2))
            sage: BD.is_t_design(return_parameters=True)
            (True, (2, 8, 2, 1))
            sage: BD = designs.AffineGeometryDesign(3, 2, GF(2))
            sage: BD.is_t_design(return_parameters=True)
            (True, (3, 8, 4, 1))
        With an integer instead of a Finite Field:
            sage: BD = designs.AffineGeometryDesign(3, 2, 4)
            sage: BD.is_t_design(return_parameters=True)
            (True, (2, 64, 16, 5))
    '''
    if type(F) is int:
        F = GF(F, 'a')
    D = ProjectiveGeometryDesign(n, d, F)
    projBlocks = D.blocks()
    blocks = [[x for x in block if x[0] != 0] for block in projBlocks]
    return IncidenceStructure([block for block in blocks if block]).relable()
