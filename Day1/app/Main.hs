import Day2 

main :: IO ()
main = do
    input <- readFile "test2.txt"
    --print (fst $ solve input)
    print (solve input)