module Day4 where









solve :: [String] -> (Int, [String])
solve input = 
    let 
        emp = (replicate (length $ head input) '.')
        input' =  map (\line -> ('.' : line) ++ "." ) ((emp : input) ++ [emp])

        inner :: [String] -> (Int,[String]) -> (Int,[String])--, [String])
        inner table (accSum,accTable)= 
            let 
                --fst res for part 1, snd res for part 2
                helper :: String -> String -> String -> (Int, String) -> (Int, String)
                helper l0 l1 l2 (accInt,accStr) = 
                    case (l0,l1,l2) of 
                        (x0 : x1 : x2 : xs, y0 : y1 : y2 : ys, z0 : z1 : z2 : zs) -> 
                            let 
                                inc = if y1 == '@' then (if (length ( filter (\x -> x =='@')(x0 : x1 : x2 : y0 : y2 : z0 : z1 : z2 : []))) < 4 then 1 else 0) else 0
                            in helper(x1 : x2 : xs) (y1 : y2 : ys) (z1 : z2 : zs) (accInt + inc, (if inc == 0 then y1 else 'x') : accStr)
                        (_,y0 : y1 : ys,_) -> (accInt, y1 : accStr)
                in 
                    case table of 
                        l0 : l1 : l2 : lx -> 
                            let 
                                result = helper l0 l1 l2 (0,head l1 : [])
                            in inner (l1 : l2 : lx) (accSum + (fst $ result), (reverse (snd $ result)) : accTable)
                        _ -> (accSum,(('.' : '.' : emp) : reverse accTable) ++ ['.' : '.' : emp])


        --(res, debug) = inner input' (0,[])
        (fin,new) = inner input' (0,[])

        final :: [String] -> [String] -> Int -> (Int,[String])
        final old new accIter = 
            if old == new then (accIter,old)
            else 
                let (a,b) = inner new (0,[])
                in final new (b) (accIter+a)
        


    --in (res,debug)
    in final input' new fin 