module Day7 where

import Data.Maybe
import Data.List

inner :: String -> [Int] -> [Int]
inner tree worlds = do
    case (tree, worlds) of 
        --'^' case
        ((_ : '^' : c2 : cs), (x0 : _ : x2 : xs)) -> 
            x0 : inner ('^' : c2 : cs) ((x0+x2) : x2 : xs) 
        --'.' case
        ((_ : c1 : c2 : cs), (x0 : x1 : x2 : xs)) -> 
            x0 : inner (c1 : c2 : cs) (x1 : x2 : xs) 
        (_, w) -> w      

solve :: [String] -> (Int,[[Int]]) 
solve input = 
    let 
        rev = reverse input 
        initial = replicate (length $ head rev) (1::Int)
        sIndex = fromJust (elemIndex 'S' $ head input)
        solveTable :: [String] -> [Int] -> [[Int]]
        solveTable table accLine = 
            case table of 
                [] -> []
                (line : rest) -> 
                    accLine : solveTable rest (inner line accLine)

        --tail simply because first accLine always uninteresting
        res = tail $ solveTable (tail rev) initial
    in (head (reverse res) !! sIndex,res)
