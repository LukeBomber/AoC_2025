module Day2 where

import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Void
import Data.NumberLength
import Text.Regex.PCRE



type Parser = Parsec Void String

pRange :: Parser (Int, Int)
pRange = (do 
    f <- read <$> some digitChar 
    _ <- string "-"
    s <- read <$> some digitChar 
    _ <- optional $ string ","
    pure $ (f,s)) 

pInput :: Parser [(Int, Int)] 
pInput = many (pRange)

outer :: (Int,Int) -> Int 
outer (lb, ub) = solveOne (lb,ub) 0

solveOne :: (Int,Int) -> Int -> Int 
solveOne (lb,ub) acc = 
    if lb>ub then acc
    else 
        if (((show lb) =~ "^([0-9]+)\\1+$") :: Bool)
            then solveOne (lb+1,ub) (acc+lb)
        else solveOne (lb+1,ub) acc


solve :: String -> (Int, Maybe [Int])
solve input = 
    case runParser pInput "input" input of 
        Left _ -> undefined
        Right xs -> 
            let ys = map (outer) xs
            in (sum ys,Just ys)
