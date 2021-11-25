import axios from 'axios'

const http = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
        'Content-type': 'application/json',
    },
})

http.interceptors.request.use(
    (request) => {
        return request
    },
    (error) => {
        throw error
    }
)

http.interceptors.response.use(
    (response) => {
        return response
    },
    (error) => {
        // Unauthorized
        if (error === 401) {
            console.log(error)
        } else {
            throw error
        }
    }
)

export default http
