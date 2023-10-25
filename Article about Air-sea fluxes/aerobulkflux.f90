program aerobulkflux
USE mod_aerobulk

implicit none

REAL(8) :: zt, zu
REAL(8),  DIMENSION(86400, 1) :: Ts, T, Humd, P, u, v, QL, QH, Tau_x, Tau_y, Evap
INTEGER :: nx, ii
nx = 86400
zt = 20
zu = 20

open (1, file='all_sto_temp_2021-08-23.csv')
DO ii=1,nx
   read(1, *) &!'(f1.2,f1.2,f2.2,f3.2, f4.2, f3.1)') &
        & Ts(ii,1), T(ii,1) , u(ii,1), v(ii,1), P(ii,1), Humd(ii,1)
      v(ii, 1) = 0
      Ts(ii, 1) = Ts(ii, 1) + 273.15
      T(ii, 1) = T(ii, 1) + 273.15
      P(ii,1) = P(ii,1) * 100
      PRINT*, Ts(ii,1), T(ii,1), u(ii,1), v(ii,1), P(ii,1), Humd(ii,1)
      !if(io.gt.0)then
      !    print*, 'Something is going wrong'
      !    exit
      !elseif(io.lt.0)then
      !    print*, 'Reached the end of file'
      !    exit
      !else
      !endif
ENDDO
close(1)


CALL aerobulk_model(jt=1, Nt=nx, calgo='coare3p0', zt=zt, zu=zu, sst=Ts, t_zt=T, hum_zt= Humd, U_zu=u, V_zu=v, slp=P, &
      & QL=QL, QH=QH, Tau_x=Tau_x, Tau_y=Tau_y, Evap=Evap, Niter=4, l_use_skin=.False.)
open(2, file='output.txt')
DO ii=1, nx
      write(2,*) QL(ii,1), QH(ii,1),Tau_x(ii,1),Tau_y(ii,1)
ENDDO
!write(2,*) 'QH=', QH ! 'QL=',QL, 'Tau_x=',Tau_x, 'Tau_y=',Tau_y
close(2)

end program aerobulkflux
