--import Day1
--import Day2 
--import Day7
import Day3

printTable :: Show a => [a] -> IO ()
printTable [] = print()
printTable [line] = print $ show line
printTable (line:xs) = (print $ show line) >> printTable xs

main :: IO ()
main = do
    let test = False

    let path = (if test then "test" else "input") ++ "3.txt"
    input <- fmap lines (readFile path)
    let res = solve input
    print $ fst $ res
    print $ snd $ res