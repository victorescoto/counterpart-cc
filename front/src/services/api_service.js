
import axios from "axios";

const instance = axios.create({
    baseURL: 'http://localhost:8000'
});

export const getCities = () => {
    return instance.get("city");
}

export const createCity = ({ name, lat, lon }) => {
    return instance.post("city", { name, lat, lon });
}

export const getSearches = () => {
    return instance.get("search");
}

export const doSearch = ({ city, startDate, endDate }) => {
    return instance.post("search", {
        city_id: city,
        start_date: startDate,
        end_date: endDate
    });
}
