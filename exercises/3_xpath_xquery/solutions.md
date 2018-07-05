# Assignment 3: XPath and XQuery

## 1.

    //city[parent::province]

## 2.

    //province/city

## 3.

    //city[located_at/@type = 'sea']

## 4.

    for $city in //city
    where $city/located_at/@type = 'sea'
    return $city

## 5.

    element seas {
        for $sea in //sea
        let $cities := //city[located_at/@water = $sea/@id]
        let $count := count($cities)
        order by $count descending
        where $count > 0
        return element sea {
            attribute name { $sea/@name },
            attribute cities { count($cities) }
        }
    }

## 6.

    element capitals_at_sea {
        for $city in //city
        where $city/located_at/@type = 'sea'
        and $city/@id = //country/@capital
        order by number($city/population) descending
        return $city
    }
