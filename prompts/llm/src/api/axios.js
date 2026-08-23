import axios from 'axios'

// Backend Django dev server default port
const BASE_URL = "http://127.0.0.1:8000"

export default axios.create({
    baseURL: BASE_URL
});
