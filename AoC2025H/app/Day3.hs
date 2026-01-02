module Day3 where

import Text.Megaparsec
import Text.Megaparsec.Char
import Data.Void
import Data.Char (digitToInt)


type Parser = Parsec Void String
 
pInput :: Parser [Int]
pInput = many (digitToInt <$> digitChar)

maxAndWhere :: [Int] -> Int -> (Int, Int) -> (Int,Int)
maxAndWhere [] _ (themax,index) = (themax,index)
maxAndWhere _ _ (9,index) = (9,index)
maxAndWhere (x:xs) cur (themax,index) = 
    maxAndWhere xs (cur+1) (if x>themax then (x,cur) else (themax,index))

handle :: [Int] -> Int -> String -> String
handle _ 0 accstr = accstr
handle [] _ _ = error "should never occur"
handle batteries rounds accstr = 
    let
        searchSpace = (length batteries) - rounds + 1
        (x,y) = maxAndWhere (take searchSpace batteries) 0 (batteries !! 0,0)
    in handle (drop (y+1) batteries) (rounds-1) ((show x) ++ accstr)

solve :: [String] -> (Int, [Int])
solve input = 
    let 
        x =
            map (\line -> case (runParser pInput "input" line)  of 
            Left _ -> undefined
            Right xs -> xs)
            input
        res = map (\inp -> read $ reverse(handle inp 12 "")) x
    in (sum res, res)
 