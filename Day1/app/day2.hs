module Day2 where

import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Void
import Data.NumberLength


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


sumRange :: (Int,Int) -> Int 
sumRange (lb,ub) = 
    let lb_len = (let temp = numberLength lb in temp + (temp `mod` 2))
        ub_len = (let temp = numberLength ub in temp - (temp `mod` 2))
    in  



solve :: String -> (Int, Maybe [Int])
solve input = 
    case runParser pInput "input" input of 
        Left _ -> undefined
        Right xs -> 
            let ys = map (sumRange) xs
            in (sum ys,Just ys)