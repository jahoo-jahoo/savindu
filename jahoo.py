U
    �m[_P  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� dZdZdZdZeD ]$Z	ej
�e	� ej
��  e �d� q>dZeed	��Zeed
��Zdd� ZdZe�  z&edd�Zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX dZdZededdd� eD ]&Z	ej
�e	� ej
��  e �d� �q zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX z&edd�Zedd�Ze�� Zej W nJ   eed��Zedd�Ze�e� ej edd�Ze�� Zej Y nX zd dl Z W nB e!k
�rp   ed� e�d� ed� e�d� d dl Z Y nX zd d l"m"Z" W nB e!k
�r�   e�d!� ed� e�d� d d l"m"Z" eZ#Y nX d"d#� Z$d$d%� Z%e&d&k�r�e$�  dS )'�    N�clearaZ  
                    ****    ***    ****    ** ** ** **    ** *     **       
                     ***    ***     ***    **       **    ** **    **       
                      ***  ** **   ***     **       **    **  **   **       
                        ***      ***       **       **    **   **  **       
                         *        *        ** ** ** **    **    ** **       

                    *** **  **          * *      ** ** ** ** **         * *
                     **       **       ** **           **              ** **
                     **        **     **   **          **             **   **
                     **        **    **     **         **            **     **
                     **       **    ** ** ** **        **           ** ** ** **
                    *** ** **      **         **       **          **         **
a-  
                    ** *     **   ** ** ** **   ** ** ** ** **
                    ** **    **   **       **         **        
                    **  **   **   **       **         **                     
                    **   **  **   **       **         **        
                    **    ** **   ** ** ** **         **            

                    *** **  **          * *      ** ** ** ** **         * *
                     **       **       ** **           **              ** **
                     **        **     **   **          **             **   **
                     **        **    **     **         **            **     **
                     **       **    ** ** ** **        **           ** ** ** **
                    *** ** **      **         **       **          **         **
zG[1;36;40m
___________________________________________________________
z:first pay R.s.100/= because create virtual own ip for you
皙�����?z*please enter correct username and passwordzEnter UserName : zEnter Password : c                  C   s�   t dkrtdkrtd� nltD ]$} tj�| � tj��  t�	d� qt
d�}|dks\|dkrht�d� n|d	ksx|d
kr�t�  nt�  d S )NZjahooZ	jahoo9808zpassword okr   z/
Are you reenter user name and password (Y/N): �Y�yzpython jahoo.py�N�n)�username�p�print�inca�sys�stdout�write�flush�time�sleep�input�os�system�exit�login)�charZreenter� r   �jahoo.pyr   6   s    

r   z192.23.55.12z	name1.dat�rz'[1;35;40mEnter your name :- [1;33;40m�wa0  [0;31;40m       Warning...


[0;31;40m Don't use Same time when Algorithm is running  in one sim 

[0;36;40m Don't use vpn

 Don't turn off the mobile data when Algorithm is running

[0;36;40m Detalis

[0;32;40m Not hacking

 Dialog user only

 version 2.1.0

 Junior script


  Create by Jahoo	2020zCreate by R*v*ndu J*y*shan

 z

[0;36;40mpaid ok  
welcom   zM[0;33;40m
        [0;32;40m
                     please follow intruction

� ��end皙�����?zfile_auth.txtz"[1;0;40m
Paste Your Auth here :- zfile_url.txtz
Paste Your URL here :- zwaiting.......zpip3 install requestsz%s Requests installed.)�tqdmzpip3 install tqdmc               	   C   s0  t �d� tD ]$} tj�| � tj��  t�d� qdt	dd�}t
}ttd��}d}d}t||�D �]�}t �d� tt� d}|dkr�tdt� td	� td
ddd�}td
�D ]@}|�d�|�� |�d� |d
 d }	t�d� tj�d� q�qbtj||d�}
t|
�}|dk�r@tD ]&} tj�| � tj��  t�d� �qnX|dk�r�|d7 }tD ]&} tj�| � tj��  t�d� �qVntt� td� tt� |d7 }tdt|�d� tdt|d �ddddd� td
ddd�}td
�D ]6}|�d�|�� |�d� |d
 d }	t�d� �q�t �d� qbt�  d S )Nr   r   zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionz[1;30;40mEnter Amount - r   zconnected ip : z6[1;34;47mChange secure connection 
Opening Algorithm
�Z   F)ZtotalZpositionZleavez
lording...�   �d   g      �?z[F)Zheadersz<Response [204]>g-C��6?z<Response [200]>zC
[1;31;40m [retry] Check Again your internet connection... [retry]z[1;32;40m
NUMBER of Message : z   z[1;32;40m
request: z 
� zWait For Next request r   r   )r   r   �namer   r   r   r   r   r   �	file_auth�	file_url1�intr   �ranger
   �ipr    Zset_description�format�update�requests�get�str�no_data�won_data�line�again)r   �headZurl�s�mZrr�sizeZloop�jZrrrZrjZrequestr   r   r   �main�   sl    

 �








r9   c                  C   sT   t �d� td�} | dks"| dkr*t�  n&| dks:| dkrBt�  ntd� t�  d S )Nr   z*[1;0;40m
Do Restart Algorithm :  (y/n) - r   r   r   r   z[1;30;40mReEnter)r   r   r   r9   �quitr
   r3   )�rer   r   r   r3   �   s    
r3   �__main__)'r   Zurllibr   r   r   r1   r0   r2   Zwarr   r   r   r   r   r   r/   r   r   r	   r   r*   �open�f�readZname1�close�wr�messager%   r
   r&   r'   r-   �ImportErrorr    Zauthr9   r3   �__name__r   r   r   r   �<module>   s�   
























A
