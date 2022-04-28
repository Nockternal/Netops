import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useParams } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card, ListGroupItem} from 'react-bootstrap'
import Rating from '../components/Rating'
//import products from '../products'
import axios from 'axios'


function ProductScreen({ match }) {
    const { id } = useParams()
    //const currentproduct = products.find((x) => x._id === id);
    const [product, setProduct] = useState([])
    useEffect(() => {
        console.log('fetching data')
        async function fetchProduct() {
        const { data } = await axios.get('/api/products/' + id)
        setProduct(data)
        console.log(data)
        }
        fetchProduct()
        
    }, [])

    return (
        <div>
            <Link to='/' className='btn btn-light my-3'>Back</Link>
            <Row>
                <Col md={6}>
                    <Image src={product.image} alt={product.name} fluid />
                </Col>
                <Col md={3}>
                    <ListGroup variant='flush'>
                        <ListGroup.Item>
                            <h3>{ product.name }</h3>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            <Rating value={ product.rating } text={ `${product.numReviews} reviews` } color={ '#f8e825' }> </Rating>
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Price: R { product.price }
                        </ListGroup.Item>
                        <ListGroup.Item>
                            Description: { product.description }
                        </ListGroup.Item>
                    </ListGroup>
                </Col>
                <Col md={3}>
                    <Card>
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <Row>
                                    <Col>Price: 
                                    </Col>
                                    <Col>
                                        <strong>
                                            R { product.price }
                                        </strong>
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Row>
                                    <Col>Status: 
                                    </Col>
                                    <Col>
                                        { product.countInStock > 0 ? 'In Stock' : 'Out of Stock' }
                                    </Col>
                                </Row>
                            </ListGroup.Item>
                            <ListGroup.Item>
                                <Button className='btn btn-block' disabled={product.countInStock === 0} type='button'>Add to Cart</Button>
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>
                </Col>
            </Row>
        </div>
  )
}

export default ProductScreen