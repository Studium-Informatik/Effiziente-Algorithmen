## PR
$$\displaylines{
Pr[f,g](\vec{x},0)&=&f(\vec{x})\\
h(\vec{x},n+1)&=&g(\vec{x},n,h(\vec{x},n))
}$$


### pred
$$pred(n)=\begin{cases}
    0   &, n=0 \\
	n-1 &, n\geq 1
  \end{cases}$$
$Pr[f,g]$ mit
$f=const_{0}^0=0$
$g(\vec{x},n,pred())=$



### add
$$add(m,n)=\begin{cases}
    m   &, n=0 \\
	suc(add(m,n-1)) &, n > 0
  \end{cases}$$

$add=Pr[f,g]$
$f=pr^1_{1}$
$g=suc \circ pr ^3_{3}$


## $\delta^k$
$\delta:\mathbb{N}\to \mathbb{N} \in \mathcal{PF}$
$\delta^k(x)=f(x,k)$  $\implies \delta$  k mal auf x anwenden

$f_{\delta}(x,0)=x$
$f_{\delta}(x,k+1)=\delta(f(x,k))$

$Pr[pr_{1}^1, \delta \circ pr_{3}^3]$


## Stacks
$f(n,0)=1$
$\delta(\langle s,l+1, \langle \langle n_{0},m_{0} \rangle, \dots, \langle n_{l-1},m_{l-1} \rangle, \langle n,0 \rangle \rangle \rangle)=$
$\delta(\langle s,l+1, \langle w, \langle n,0 \rangle \rangle \rangle)=\langle s+1,l+1,w \rangle$

$\delta(\langle s,l+1,\langle w,\langle 0,n \rangle \rangle \rangle)=\langle s,l+1,w \rangle$

$\delta(\langle s,l+1,\langle w,\langle n+1,m+1 \rangle \rangle \rangle)=\langle s,l+2,\langle w,\langle n,m \rangle, \langle n,m+1 \rangle \rangle \rangle$


## Minimierung
$$
Mn[\varphi](\vec{x},n)=\begin{cases}
min \{ m\leq n \mid \varphi(\vec{x},n) \} & \text{, falls }\varphi \\ \\
n+1 & \text{, sonst}
\end{cases}
$$

$$\displaylines{
f(x)&=&x^{2}\\ \\
f(x)^{-1}&&x\\
x&&f(x)\\
0 && 0\\
1 && 1\\
2 && 4\\
3 && 9\\
4 && 16\\
}$$


$f^{-1}(x)=\lceil \sqrt{ x } \rceil=\{ m \leq x \mid m^{2} \geq x \}$
$\varphi=\geq \circ (mult \circ (pr_{2}^2, pr_{2}^2), pr_{1}^2)$

$n=x$
$Mn[\varphi](x,x)$
$f^{-1}=Mn[\varphi] \circ (pr_{1}^{1},pr_{1}^{1})$

$$\mu f(\vec{x})=\begin{cases}
m    &, min\{ m \mid f(\vec{x}, m)=0 \} \quad 1\dots \\
\bot
\end{cases}$$

$\mu f(\vec{x})=Mn[= \circ (f, const_{0}^{2})](\vec{x})$

