# Setting up

First we need to deploy a python environment to run everything

We will create the next script

```jsx
#!/bin/bash
python3 -m venv v_env
source v_env/bin/activate
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "env created"
    pip install matplotlib
    echo "requierements installed"
else
    echo "env is not working!"
fi
```

This library will make our data visual, more info [here](https://matplotlib.org/)

## Estimate.py

This function will predict the price of a car based on its milleage using the next function

$$
estimatePrice(mileage) = θ_0 + (θ_1 ∗ mileage)
$$

Which is a basic linear function

$$
𝑦=𝜃_0+𝜃_1𝑥
$$

Note: Before running the training program `theta0` and `theta1` will be set to 0

## Train.py

This function will train the model using a dataset and performing a linear regresion.

Once the linear regresion is completed, `theta0` and `theta1` will be stored to use in `estimate.py` 

We will use the Mean Absolute Error (MAE) function as a loss function (a loss function is used to see how precise is our model)

$$
MAE = \frac{1}{m}  \sum_{i=1}^{m} | \hat{y_{i}} - y_{i} |
$$

Where:

- *m* is the number of samples
- $ŷ_i$ is the predicted value
- $y$ is the actual value

What this function will do is: estimate the price, substract it to the actual price and make it absolute, do it for all the data points we gave, and divide the sum by the number of data points.

For example, having 3 data points:

- $y_1$ = 2000 and $ŷ_1$ = 1800
- $y_2$ = 4000 and $ŷ_2$ = 3800
- $y_3$ = 6000 and $ŷ_3$ = 6200

The MAE will be:

$$
𝑀𝐴𝐸=\frac {|2000−1800|+|4000−3800|+|6000−6200|} 3 = 200
$$

Here, the MAE is 200, so we know our model is off by 200 on average

> Unless your dataset is perfectly aligned, the MAE will never be 0
> 

Now that we can measure the precision we have to find the best $𝜃_0$ and $𝜃_1$ that makes the loss function the minimum

## Gradient Descent

Gradient descent is an optimization algorithm that consists in finding the minimum of a function by iteratively getting closer to it.

In this case we will optimize our loss function.

The algorithm will do this:

1. Initialize the $θ_0$ and $θ_1$ to 0
2. Calculate de gradient of the loss function, in other words, “what do $θ_0$ and $θ_1$ miss to be optimal?”
3. Update $θ_0$ and $θ_1$ in the opposite direction of the gradient (substraction)
4. Repeat steps 2 and 3 until the loss function converges

The formula to update the $θ_0$ and $θ_1$ is:

$$
θ_0 = θ_0 - \alpha \frac{1}{m}  \sum_{i=1}^{m} ( \hat{y_{i}} - y_{i} )
$$

$$
θ_1 = θ_1 - \alpha \frac{1}{m}  \sum_{i=1}^{m} (( \hat{y_{i}} - y_{i} ) * x_i)
$$

Where:

- $\alpha$ is the learning rate
- $m$ is the number of samples
- $\hat{y}$  is the predicted value
- $y$  is the actual value
- $x$ is the feature

> The learning rate controls how much we update the $θ_0$ and $θ_1$ at each iteration.
If it’s too high we might overshoot the minimum, if it’s too low, it might take too long to converge.
> 

Why using these formulas to update the $θ_0$ and $θ_1$?

- $θ_0$ is updated straightforward, it’s the average of the errors: if our line is ≈ 200 above the actual values we just need to lower it by 200
- $θ_1$ is updated a bit differently because it has a coefficient. We need to correct that offset, but also its slope (how inclined it is)

> These formulas are the ones given by the subject
> 

## Feature Scaling

We have a new problem now, because implementing it like it is now we have mileage in thousands and price is in tens of thousands. Meaning that  $θ_0$ is updated more for the milleage than for the price.

To avoid this we have to scale the features.

We will use the standarization method

 

$$
x_{scaled} = \frac {x - μ}{σ}
$$

Where:

- $x$ is the feature
- $μ$ is the mean of the feature
- $σ$ is the standard deviation of the feature

> The mean is used to center the data around 0

The standard deviation is used to scale the data, so it has a variance of 1
> 

For example, having the following data:

- *mileage = [2000, 4000, 6000]*
- 𝜇 = 4000
- $σ$ = 1632.99

The formula for the standard deviation is the following

$$
σ = \sqrt{\sum\frac{(x_i - 𝜇)²}N}
$$

The scaled mileage would be:

$$
milleage_{scaled}=[\frac{2000-4000}{1632.99},\frac{4000-4000}{1632.99},\frac{6000-4000}{1632.99}] = [-1.22, 0, 1.22]
$$

## Wrap up

Knowing everything we need for the project we will summarize the steps to implement the linear regression:

1. Load the data
2. Scale the feature (mileage)
3. Initialize $θ_0$ and $θ_1$ to 0
4. Make a naive prediction of price: $θ_0$ + $θ_1$ * milleage for every datapoint
5. Calculate the average error
6. Update $θ_0$ and $θ_1$ accordingly
7. Repeat steps 4 to 6 until the loss converges
8. Save $θ_0$ and $θ_1$ into a file

## Resources

[Gradient Descent, Step-by-Step](https://www.youtube.com/watch?v=sDv4f4s2SB8)

[How Neural Networks Learn using Gradient Descent](https://bhatnagar91.medium.com/how-neural-networks-learn-using-gradient-descent-f48c2e4079a6)